# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(972, 657)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setMinimumSize(QtCore.QSize(80, 0))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.txt_ruta = QtWidgets.QLineEdit(self.tab)
        self.txt_ruta.setObjectName("txt_ruta")
        self.horizontalLayout.addWidget(self.txt_ruta)
        self.btn_rutaExaminar = QtWidgets.QPushButton(self.tab)
        self.btn_rutaExaminar.setMinimumSize(QtCore.QSize(200, 0))
        self.btn_rutaExaminar.setObjectName("btn_rutaExaminar")
        self.horizontalLayout.addWidget(self.btn_rutaExaminar)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_buscar = QtWidgets.QPushButton(self.frame)
        self.btn_buscar.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_buscar.setObjectName("btn_buscar")
        self.gridLayout.addWidget(self.btn_buscar, 0, 0, 1, 2)
        self.btn_buscarPestanaNueva = QtWidgets.QPushButton(self.frame)
        self.btn_buscarPestanaNueva.setMinimumSize(QtCore.QSize(0, 26))
        self.btn_buscarPestanaNueva.setObjectName("btn_buscarPestanaNueva")
        self.gridLayout.addWidget(self.btn_buscarPestanaNueva, 1, 0, 1, 2)
        self.btn_pausar = QtWidgets.QPushButton(self.frame)
        self.btn_pausar.setMinimumSize(QtCore.QSize(0, 26))
        self.btn_pausar.setObjectName("btn_pausar")
        self.gridLayout.addWidget(self.btn_pausar, 2, 0, 1, 1)
        self.btn_parar = QtWidgets.QPushButton(self.frame)
        self.btn_parar.setMinimumSize(QtCore.QSize(0, 26))
        self.btn_parar.setObjectName("btn_parar")
        self.gridLayout.addWidget(self.btn_parar, 2, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 1, 4, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setMinimumSize(QtCore.QSize(80, 0))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.txt_excluirRuta = QtWidgets.QLineEdit(self.tab)
        self.txt_excluirRuta.setObjectName("txt_excluirRuta")
        self.horizontalLayout_2.addWidget(self.txt_excluirRuta)
        self.btn_excluirExaminar = QtWidgets.QPushButton(self.tab)
        self.btn_excluirExaminar.setMinimumSize(QtCore.QSize(200, 0))
        self.btn_excluirExaminar.setObjectName("btn_excluirExaminar")
        self.horizontalLayout_2.addWidget(self.btn_excluirExaminar)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setMinimumSize(QtCore.QSize(80, 0))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.txt_incluirArchivos = QtWidgets.QLineEdit(self.tab)
        self.txt_incluirArchivos.setObjectName("txt_incluirArchivos")
        self.horizontalLayout_3.addWidget(self.txt_incluirArchivos)
        self.cb_incluirArchivos = QtWidgets.QComboBox(self.tab)
        self.cb_incluirArchivos.setMinimumSize(QtCore.QSize(200, 0))
        self.cb_incluirArchivos.setObjectName("cb_incluirArchivos")
        self.horizontalLayout_3.addWidget(self.cb_incluirArchivos)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setMinimumSize(QtCore.QSize(80, 0))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.txt_consulta = QtWidgets.QLineEdit(self.tab)
        self.txt_consulta.setObjectName("txt_consulta")
        self.horizontalLayout_4.addWidget(self.txt_consulta)
        self.cb_consulta = QtWidgets.QComboBox(self.tab)
        self.cb_consulta.setMinimumSize(QtCore.QSize(200, 0))
        self.cb_consulta.setObjectName("cb_consulta")
        self.horizontalLayout_4.addWidget(self.cb_consulta)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)
        self.tableSearch = QtWidgets.QTableWidget(self.tab)
        self.tableSearch.setObjectName("tableSearch")
        self.tableSearch.setColumnCount(0)
        self.tableSearch.setRowCount(0)
        self.gridLayout_2.addWidget(self.tableSearch, 4, 0, 1, 2)
        self.tabs = QtWidgets.QTabWidget(self.tab)
        self.tabs.setObjectName("tabs")
        self.tab_sumary = QtWidgets.QWidget()
        self.tab_sumary.setObjectName("tab_sumary")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_sumary)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tedit_sumary = QtWidgets.QPlainTextEdit(self.tab_sumary)
        self.tedit_sumary.setObjectName("tedit_sumary")
        self.gridLayout_5.addWidget(self.tedit_sumary, 0, 0, 1, 1)
        self.tabs.addTab(self.tab_sumary, "")
        self.tab_hints = QtWidgets.QWidget()
        self.tab_hints.setObjectName("tab_hints")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_hints)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tedit_hints = QtWidgets.QPlainTextEdit(self.tab_hints)
        self.tedit_hints.setObjectName("tedit_hints")
        self.gridLayout_4.addWidget(self.tedit_hints, 0, 0, 1, 1)
        self.tabs.addTab(self.tab_hints, "")
        self.gridLayout_2.addWidget(self.tabs, 5, 0, 1, 2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 972, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabs.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Super Grep"))
        self.label.setText(_translate("MainWindow", "Ruta: "))
        self.btn_rutaExaminar.setText(_translate("MainWindow", "Examinar"))
        self.btn_buscar.setText(_translate("MainWindow", "Buscar"))
        self.btn_buscarPestanaNueva.setText(_translate("MainWindow", "Busqueda Pestaña Nueva"))
        self.btn_pausar.setText(_translate("MainWindow", "Pausar"))
        self.btn_parar.setText(_translate("MainWindow", "Parar"))
        self.label_2.setText(_translate("MainWindow", "Excluir Ruta: "))
        self.btn_excluirExaminar.setText(_translate("MainWindow", "Examinar"))
        self.label_5.setText(_translate("MainWindow", "Excluir Archivos:"))
        self.label_6.setText(_translate("MainWindow", "Consulta:"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_sumary), _translate("MainWindow", "Sumary"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_hints), _translate("MainWindow", "Hints"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Search -"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "+"))
