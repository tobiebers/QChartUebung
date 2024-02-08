from PySide6.QtWidgets import QMainWindow
from Chart import Chart

class MyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("QChartView")

        # Set the central widget
        self.setCentralWidget(Chart(self))

        # Set the size of the main window
        self.resize(875, 620)