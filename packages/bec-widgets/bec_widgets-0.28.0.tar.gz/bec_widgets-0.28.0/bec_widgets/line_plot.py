import os
import threading
import time
import warnings
from typing import Any

import numpy as np
import pyqtgraph
import pyqtgraph as pg
from bec_lib.core import BECMessage, MessageEndpoints
from bec_lib.core.redis_connector import MessageObject, RedisConnector
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QCheckBox, QTableWidgetItem
from pyqtgraph import mkBrush, mkColor, mkPen
from pyqtgraph.Qt import QtCore, QtWidgets, uic
from pyqtgraph.Qt.QtCore import pyqtSignal
from qt_utils import Crosshair

from bec_widgets.bec_dispatcher import bec_dispatcher

client = bec_dispatcher.client


class BasicPlot(QtWidgets.QWidget):
    update_signal = pyqtSignal()
    roi_signal = pyqtSignal(tuple)

    def __init__(self, name="", y_value_list=["gauss_bpm"]) -> None:
        """
        Basic plot widget for displaying scan data.

        Args:
            name (str, optional): Name of the plot. Defaults to "".
            y_value_list (list, optional): List of signals to be plotted. Defaults to ["gauss_bpm"].
        """

        super(BasicPlot, self).__init__()
        # Set style for pyqtgraph plots
        pg.setConfigOption("background", "w")
        pg.setConfigOption("foreground", "k")
        current_path = os.path.dirname(__file__)
        uic.loadUi(os.path.join(current_path, "line_plot.ui"), self)

        self._idle_time = 100
        self.producer = RedisConnector(["localhost:6379"]).producer()

        self.y_value_list = y_value_list
        self.previous_y_value_list = None
        self.plotter_data_x = []
        self.plotter_data_y = []

        self.plotter_scan_id = None

        self._current_proj = None
        self._current_metadata_ep = "px_stream/projection_{}/metadata"

        self.proxy_update = pg.SignalProxy(self.update_signal, rateLimit=25, slot=self.update)

        self.data_retriever = threading.Thread(target=self.on_projection, daemon=True)
        self.data_retriever.start()

        # self.comboBox.currentIndexChanged.connect(lambda : print(f'current comboText: {self.comboBox.currentText()}'))
        # self.comboBox.currentIndexChanged.connect(lambda: print(f'current comboIndex: {self.comboBox.currentIndex()}'))
        #
        # self.doubleSpinBox.valueChanged.connect(lambda : print('Spin Changed'))

        # self.splitterH_main.setSizes([1, 1])

        ##########################
        # UI
        ##########################
        self.init_ui()
        self.init_curves()
        self.hook_crosshair()
        self.pushButton_generate.clicked.connect(self.generate_data)

    def init_ui(self):
        """Setup all ui elements"""
        ##########################
        # 1D Plot
        ##########################

        # LabelItem for ROI
        self.label_plot = pg.LabelItem(justify="center")
        self.glw_plot.addItem(self.label_plot)
        self.label_plot.setText("ROI region")

        # ROI selector - so far from [-1,1] #TODO update to scale with xrange
        self.roi_selector = pg.LinearRegionItem([-1, 1])

        self.glw_plot.nextRow()  # TODO update of cursor
        self.label_plot_moved = pg.LabelItem(justify="center")
        self.glw_plot.addItem(self.label_plot_moved)
        self.label_plot_moved.setText("Actual coordinates (X, Y)")

        # Label for coordinates clicked
        self.glw_plot.nextRow()
        self.label_plot_clicked = pg.LabelItem(justify="center")
        self.glw_plot.addItem(self.label_plot_clicked)
        self.label_plot_clicked.setText("Clicked coordinates (X, Y)")

        # 1D PlotItem
        self.glw_plot.nextRow()
        self.plot = pg.PlotItem()
        self.plot.setLogMode(True, True)
        self.glw_plot.addItem(self.plot)
        self.plot.addLegend()

        ##########################
        # 2D Plot
        ##########################

        # Label for coordinates moved
        self.label_image_moved = pg.LabelItem(justify="center")
        self.glw_image.addItem(self.label_image_moved)
        self.label_image_moved.setText("Actual coordinates (X, Y)")

        # Label for coordinates clicked
        self.glw_image.nextRow()
        self.label_image_clicked = pg.LabelItem(justify="center")
        self.glw_image.addItem(self.label_image_clicked)
        self.label_image_clicked.setText("Clicked coordinates (X, Y)")

        # TODO try to lock aspect ratio with view

        # # Create a window
        # win = pg.GraphicsLayoutWidget()
        # win.show()
        #
        # # Create a ViewBox
        # view = win.addViewBox()
        #
        # # Lock the aspect ratio
        # view.setAspectLocked(True)

        # # Create an ImageItem
        # image_item = pg.ImageItem(np.random.random((100, 100)))
        #
        # # Add the ImageItem to the ViewBox
        # view.addItem(image_item)

        # 2D ImageItem
        self.glw_image.nextRow()
        self.plot_image = pg.PlotItem()
        self.glw_image.addItem(self.plot_image)

    def init_curves(self):
        # init of 1D plot
        self.plot.clear()

        self.curves = []
        self.pens = []
        self.brushs = []

        self.color_list = BasicPlot.golden_angle_color(
            colormap="CET-R2", num=len(self.y_value_list)
        )

        for ii, y_value in enumerate(self.y_value_list):
            pen = mkPen(color=self.color_list[ii], width=2, style=QtCore.Qt.DashLine)
            brush = mkBrush(color=self.color_list[ii])
            curve = pg.PlotDataItem(symbolBrush=brush, pen=pen, skipFiniteCheck=True, name=y_value)
            self.plot.addItem(curve)
            self.curves.append(curve)
            self.pens.append(pen)
            self.brushs.append(brush)

        # check if roi selector is in the plot
        if self.roi_selector not in self.plot.items:
            self.plot.addItem(self.roi_selector)

        # init of 2D plot
        self.plot_image.clear()

        self.img = pg.ImageItem()
        self.plot_image.addItem(self.img)

        # hooking signals
        self.hook_crosshair()
        self.init_table()

    def splitter_sizes(self):
        ...

    def hook_crosshair(self):
        self.crosshair_1d = Crosshair(self.plot, precision=4)

        self.crosshair_1d.coordinatesChanged1D.connect(
            lambda x, y: self.label_plot_moved.setText(f"Moved : ({x}, {y})")
        )
        self.crosshair_1d.coordinatesClicked1D.connect(
            lambda x, y: self.label_plot_clicked.setText(f"Moved : ({x}, {y})")
        )

        self.crosshair_1d.coordinatesChanged1D.connect(
            lambda x, y: self.update_table(table_widget=self.cursor_table, x=x, y_values=y)
        )

        self.crosshair_2D = Crosshair(self.plot_image)

        self.crosshair_2D.coordinatesChanged2D.connect(
            lambda x, y: self.label_image_moved.setText(f"Moved : ({x}, {y})")
        )
        self.crosshair_2D.coordinatesClicked2D.connect(
            lambda x, y: self.label_image_clicked.setText(f"Moved : ({x}, {y})")
        )

        # ROI
        self.roi_selector.sigRegionChangeFinished.connect(self.get_roi_region)

    def generate_data(self):
        def gauss(x, mu, sigma):
            return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

        self.plotter_data_x = np.linspace(0, 10, 1000)
        self.plotter_data_y = [
            gauss(self.plotter_data_x, 1, 1),
            gauss(self.plotter_data_x, 1.5, 3),
            np.sin(self.plotter_data_x),
            np.cos(self.plotter_data_x),
            np.sin(2 * self.plotter_data_x),
        ]  # List of y-values for multiple curves
        self.y_value_list = ["Gauss (1,1)", "Gauss (1.5,3)"]  # ["Sine"]#, "Cosine", "Sine2x"]

        # Curves
        color_list = ["#384c6b", "#e28a2b", "#5E3023", "#e41a1c", "#984e83", "#4daf4a"]

        self.init_curves()

        for ii in range(len(self.y_value_list)):
            self.curves[ii].setData(self.plotter_data_x, self.plotter_data_y[ii])

        self.data_2D = np.random.random((150, 30))
        self.img.setImage(self.data_2D)

        if self.roi_selector not in self.plot.items:
            self.plot.addItem(self.roi_selector)

    def get_roi_region(self):
        """For testing purpose now, get roi region and print it to self.label as tuple"""
        region = self.roi_selector.getRegion()
        self.label_plot.setText(f"x = {(10 ** region[0]):.4f}, y ={(10 ** region[1]):.4f}")
        return_dict = {
            "horiz_roi": [
                np.where(self.plotter_data_x[0] > 10 ** region[0])[0][0],
                np.where(self.plotter_data_x[0] < 10 ** region[1])[0][-1],
            ]
        }
        msg = BECMessage.DeviceMessage(signals=return_dict).dumps()
        self.producer.set_and_publish("px_stream/gui_event", msg=msg)
        self.roi_signal.emit(region)

    def init_table(self):
        # Init number of rows in table according to n of devices
        self.cursor_table.setRowCount(len(self.y_value_list))
        # self.table.setHorizontalHeaderLabels(["(X, Y) - Moved", "(X, Y) - Clicked"]) #TODO can be dynamic
        self.cursor_table.setVerticalHeaderLabels(self.y_value_list)
        self.cursor_table.resizeColumnsToContents()

    def update_table(self, table_widget, x, y_values):
        for i, y in enumerate(y_values):
            table_widget.setItem(i, 1, QTableWidgetItem(str(x)))
            table_widget.setItem(i, 2, QTableWidgetItem(str(y)))
            table_widget.resizeColumnsToContents()

    def update(self):
        """Update the plot with the new data."""

        # check if QTable was initialised and if list of devices was changed
        # if self.y_value_list != self.previous_y_value_list:
        #     self.setup_cursor_table()
        #     self.previous_y_value_list = self.y_value_list.copy() if self.y_value_list else None

        self.curves[0].setData(self.plotter_data_x[0], self.plotter_data_y[0])

    @staticmethod
    def flip_even_rows(arr):
        arr_copy = np.copy(arr)  # Create a writable copy
        arr_copy[1::2, :] = arr_copy[1::2, ::-1]
        return arr_copy

    @staticmethod
    def remove_curve_by_name(plot: pyqtgraph.PlotItem, name: str) -> None:
        # def remove_curve_by_name(plot: pyqtgraph.PlotItem, checkbox: QtWidgets.QCheckBox, name: str) -> None:
        """Removes a curve from the given plot by the specified name.

        Args:
            plot (pyqtgraph.PlotItem): The plot from which to remove the curve.
            name (str): The name of the curve to remove.
        """
        # if checkbox.isChecked():
        for item in plot.items:
            if isinstance(item, pg.PlotDataItem) and getattr(item, "opts", {}).get("name") == name:
                plot.removeItem(item)
                return

        # else:
        #     return

    @staticmethod
    def golden_ratio(num: int) -> list:
        """Calculate the golden ratio for a given number of angles.

        Args:
            num (int): Number of angles
        """
        phi = 2 * np.pi * ((1 + np.sqrt(5)) / 2)
        angles = []
        for ii in range(num):
            x = np.cos(ii * phi)
            y = np.sin(ii * phi)
            angle = np.arctan2(y, x)
            angles.append(angle)
        return angles

    @staticmethod
    def golden_angle_color(colormap: str, num: int) -> list:
        """
        Extract num colors for from the specified colormap following golden angle distribution.

        Args:
            colormap (str): Name of the colormap
            num (int): Number of requested colors

        Returns:
            list: List of colors with length <num>

        Raises:
            ValueError: If the number of requested colors is greater than the number of colors in the colormap.
        """

        cmap = pg.colormap.get(colormap)
        cmap_colors = cmap.color
        if num > len(cmap_colors):
            raise ValueError(
                f"Number of colors requested ({num}) is greater than the number of colors in the colormap ({len(cmap_colors)})"
            )
        angles = BasicPlot.golden_ratio(len(cmap_colors))
        color_selection = np.round(np.interp(angles, (-np.pi, np.pi), (0, len(cmap_colors))))
        colors = [
            mkColor(tuple((cmap_colors[int(ii)] * 255).astype(int))) for ii in color_selection[:num]
        ]
        return colors

    def on_projection(self):
        while True:
            if self._current_proj is None:
                time.sleep(0.1)
                continue
            endpoint = f"px_stream/projection_{self._current_proj}/data"
            msgs = client.producer.lrange(topic=endpoint, start=-1, end=-1)
            data = [BECMessage.DeviceMessage.loads(msg) for msg in msgs]
            if not data:
                continue
            with np.errstate(divide="ignore", invalid="ignore"):
                self.plotter_data_y = [
                    np.sum(
                        np.sum(data[-1].content["signals"]["data"] * self._current_norm, axis=1)
                        / np.sum(self._current_norm, axis=0),
                        axis=0,
                    ).squeeze()
                ]

            self.update_signal.emit()

    @pyqtSlot(dict, dict)
    def on_dap_update(self, data: dict, metadata: dict):
        data_test = data

        flipped_data = self.flip_even_rows(data["z"])

        self.img.setImage(flipped_data)

    @pyqtSlot(dict, dict)
    def new_proj(self, content: dict, _metadata: dict):
        proj_nr = content["signals"]["proj_nr"]
        endpoint = f"px_stream/projection_{proj_nr}/metadata"
        msg_raw = client.producer.get(topic=endpoint)
        msg = BECMessage.DeviceMessage.loads(msg_raw)
        self._current_q = msg.content["signals"]["q"]
        self._current_norm = msg.content["signals"]["norm_sum"]
        self._current_metadata = msg.content["signals"]["metadata"]

        self.plotter_data_x = [self._current_q]
        self._current_proj = proj_nr


if __name__ == "__main__":
    import argparse

    from bec_widgets import ctrl_c

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--signals", help="specify recorded signals", nargs="+", default=["gauss_bpm"]
    )
    # default = ["gauss_bpm", "bpm4i", "bpm5i", "bpm6i", "xert"],
    # dispatcher = bec_dispatcher
    value = parser.parse_args()
    print(f"Plotting signals for: {', '.join(value.signals)}")
    client = bec_dispatcher.client
    app = QtWidgets.QApplication([])
    ctrl_c.setup(app)
    plot = BasicPlot(y_value_list=value.signals)

    bec_dispatcher.connect_slot(plot.new_proj, "px_stream/proj_nr")
    bec_dispatcher.connect_slot(
        plot.on_dap_update, MessageEndpoints.processed_data("px_dap_worker")
    )
    plot.show()
    # client.callbacks.register("scan_segment", plot, sync=False)
    app.exec_()
