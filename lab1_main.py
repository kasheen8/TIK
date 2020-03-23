# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, Qt
from lab1_form import Ui_MainWindow
import math_module

class mywindow(QtWidgets.QMainWindow): #класс приложения
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.spinBox.valueChanged.connect(self.spinBox_value_change)
        self.ui.spinBox_2.valueChanged.connect(self.spinBox2_value_change)
        self.ui.spinBox_3.valueChanged.connect(self.spinBox3_value_change)
        self.ui.spinBox_4.valueChanged.connect(self.spinBox4_value_change)
        self.ui.spinBox_5.valueChanged.connect(self.spinBox5_value_change)
    def spinBox_value_change(self): #функция, срабатывающая при изменении значения n в Задаче 1, заполняющая таблицу, график и экстремумы
        _translate = QtCore.QCoreApplication.translate
        table = self.ui.tableWidget
        spinBox_value = self.ui.spinBox.value()
        if spinBox_value == 0:
            table.setColumnCount(0)
            table.setRowCount(0)
            self.ui.plotWidget.figure.clear()
            self.ui.plotWidget.canvas.draw()
            self.ui.lineEdit.clear()
            self.ui.lineEdit_2.clear()
        else:
            if spinBox_value > 7:
                table.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
                table.setFixedSize(441,75)
            else:
                table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
                table.setFixedSize(441, 61)
            table.setColumnCount(spinBox_value+1)
            table.setRowCount(2)
            table.setVerticalHeaderLabels(('X', 'P'))
            prob_list = math_module.prob_calc(spinBox_value)
            for x in range(spinBox_value + 1):
                lable1 = QtWidgets.QLabel()
                lable1.setStyleSheet('background-color: #FFFFFF;')
                lable1.setText(_translate('MainWindow', math_module.formula_to_html(prob_list[x])))
                table.setItem(0, x, self.createItem(f'{x}', Qt.ItemIsSelectable))
                table.setCellWidget(1,x,lable1)
                table.resizeColumnsToContents()
            graph_coord = math_module.entropy_graph(prob_list)
            self.ui.plotWidget.plot(graph_coord)
            self.ui.lineEdit.setText(f'{round(max(graph_coord[1]),2)}')
            self.ui.lineEdit_2.setText(f'{min(graph_coord[1])}')

    def spinBox2_value_change(self): #функция, срабатывающая при изменении значения n в Задаче 2, заполняющая таблицу, график и экстремумы
        _translate = QtCore.QCoreApplication.translate
        table = self.ui.tableWidget_2
        spinBox_value = self.ui.spinBox_2.value()
        if spinBox_value == 0:
            table.setColumnCount(0)
            table.setRowCount(0)
            self.ui.plotWidget_2.figure.clear()
            self.ui.plotWidget_2.canvas.draw()
            self.ui.lineEdit_3.clear()
            self.ui.lineEdit_4.clear()
        else:
            table.setColumnCount(spinBox_value)
            table.setRowCount(2)
            table.setVerticalHeaderLabels(('X', 'P'))
            prob_list = math_module.prob_calc_zero(spinBox_value)
            for x in range(1, spinBox_value + 1):
                lable1 = QtWidgets.QLabel()
                lable1.setStyleSheet('background-color: #FFFFFF;')
                lable1.setText(_translate('MainWindow', math_module.formula_to_html(prob_list[x])))
                table.setItem(0, x-1, self.createItem(f'{x}', Qt.ItemIsSelectable))
                table.setCellWidget(1, x-1, lable1)
                table.resizeColumnsToContents()
            graph_coord = math_module.entropy_graph(prob_list)
            self.ui.plotWidget_2.plot(graph_coord,ylim_max = 5)
            self.ui.lineEdit_3.setText(f'{round(max(graph_coord[1]), 2)}')
            self.ui.lineEdit_4.setText(f'{min(graph_coord[1])}')

    def spinBox3_value_change(self): #функция, срабатывающая при изменении значения n в Задаче 3, заполняющая таблицу, график и экстремумы
        spinboxChangeValue_details(self.ui)

    def spinBox4_value_change(self): #функция, срабатывающая при изменении значения m в Задаче 2, заполняющая таблицу, график и экстремумы
        spinboxChangeValue_details(self.ui)

    def spinBox5_value_change(self): #функция, срабатывающая при изменении значения k в Задаче 2, заполняющая таблицу, график и экстремумы
        spinboxChangeValue_details(self.ui)


    def createItem(self, text, flags): #функция для добавления элементов в таблицы
        tableWidgetItem = QtWidgets.QTableWidgetItem(text)
        tableWidgetItem.setFlags(flags)
        return tableWidgetItem

def spinboxChangeValue_details(self): #функция, срабатывающая при изменении значений в 3 задаче
    self.spinBox_4.setMaximum(self.spinBox_3.value())
    self.spinBox_5.setMaximum(self.spinBox_3.value())
    table = self.tableWidget_3
    graph = self.plotWidget_3
    n = self.spinBox_3.value()
    m = self.spinBox_4.value()
    k = self.spinBox_5.value()
    if n == 0:
        table.setColumnCount(0)
        table.setRowCount(0)
        graph.figure.clear()
        graph.canvas.draw()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
    else:
        table.setColumnCount(m + 1)
        table.setRowCount(2)
        table.setVerticalHeaderLabels(('X', 'P'))
        prob_list = math_module.prob_calc_stand_part(n, m)
        for x in range(m+1):
            table.setItem(0, x, mywindow.createItem(self,f'{x}', Qt.ItemIsSelectable))
            table.setItem(1, x, mywindow.createItem(self,f'{round(prob_list[k][x],2)}', Qt.ItemIsSelectable))
            font = QtGui.QFont()
            font.setFamily("Times New Roman")
            font.setPointSize(14)
            font.setBold(True)
            table.item(1, x).setFont(font)
            table.resizeColumnsToContents()
        graph_coord = math_module.entropy_graph_for_details(prob_list)
        self.plotWidget_3.plot(graph_coord, ylim_max=2, xlim_max=n, plot_label = 'H(k)', x_locator=1)
        self.lineEdit_5.setText(f'{round(max(graph_coord[1]), 2)}')
        self.lineEdit_6.setText(f'{min(graph_coord[1])}')




app = QtWidgets.QApplication(sys.argv)
application = mywindow()
application.show()

sys.exit(app.exec_())