# -*- coding: utf-8 -*-
import sys
import os

from PyQt5.QtGui import QFont, QIcon, QColor, QPalette, QPixmap, QTextCharFormat, QBrush, QTextCursor
from PyQt5.QtCore import (QProcess, Qt, pyqtSignal, QMimeData, pyqtSlot, QThread, QRegExp, QTextCodec, QObject)
from PyQt5.QtWidgets import (QApplication, QMainWindow, QMessageBox, QFileDialog, QLineEdit,
                             QTableWidgetItem, QAbstractItemView, QHeaderView, QLabel, QVBoxLayout,
                             QWidget, QFrame, QPushButton, QGridLayout, QHBoxLayout)

from PyQt5 import uic


class Ventana(QDialog):
    errorSignal = pyqtSignal(str)
    outputSignal = pyqtSignal(str)

    def __init__(self):
        QMainWindow.__init__(self)
        # Cargar la configuracion del archivo .ui en el objeto
        uic.loadUi("menu.ui", self)

if __name__ == '__main__':
    # Instancia para iniciar una aplicacion
    app = QApplication(sys.argv)
    # Crear un objeto de la clase
    _ventana = Ventana()
    # Muestra la ventana
    _ventana.show()
    # Ejecutar la aplicacion
    app.exec_()