from PySide6.QtWidgets import QWidget, QHBoxLayout
from PySide6.QtCharts import QChart, QLineSeries, QChartView, QValueAxis, QDateTimeAxis
from PySide6.QtGui import QPixmap, QPalette, QBrush
from PySide6.QtCore import Qt, QSize, QDateTime, QDate, QTime


class Chart(QWidget):
    def __init__(self, parent=None):
        super(Chart, self).__init__(parent)

        self.chart = QChart()

        series = QLineSeries()

        # Korrigierte Erstellung von QDateTime-Objekten
        dateTime1 = QDateTime(QDate(2023, 1, 1), QTime(0, 0)).toMSecsSinceEpoch()  # 1. Januar 2023
        dateTime2 = QDateTime(QDate(2023, 1, 4), QTime(0, 0)).toMSecsSinceEpoch()  # 4. Januar 2023

        series.append(dateTime1, 6)
        series.append(dateTime2, 9)

        self.chart.addSeries(series)

        axisX = QDateTimeAxis()
        axisX.setFormat("dd.MM.yyyy")
        axisX.setTitleText("Datum")
        axisX.setTickCount(5)

        axisY = QValueAxis()
        axisY.setRange(0, 10)
        axisY.setTitleText("Y-Achse")

        self.chart.setAxisX(axisX, series)
        self.chart.setAxisY(axisY, series)

        self.chartView = QChartView(self.chart)

        layout = QHBoxLayout()
        layout.addWidget(self.chartView)
        self.setLayout(layout)