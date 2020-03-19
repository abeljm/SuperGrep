import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QHeaderView, QFileDialog, QAbstractItemView
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt, pyqtSlot, pyqtSignal, QThread
from functools import partial
from interface.main import Ui_MainWindow

import re
import os
import pathlib

class SuperGrep(QMainWindow):
    def __init__(self):
        super(SuperGrep, self).__init__()
        self.ui = Ui_MainWindow()        
        self.ui.setupUi(self)
        self.tableSearch()
        self.ui.btn_rutaExaminar.clicked.connect(partial(self.browse, self.ui.txt_ruta))
        self.ui.btn_excluirExaminar.clicked.connect(partial(self.browse, self.ui.txt_excluirRuta))
        self.ui.btn_buscar.clicked.connect(self.scan)

    def browse(self,edit):
        fileName = QFileDialog.getExistingDirectory(self, 'Select directory')
        if fileName:
            edit.setText(fileName)

    def scan(self):
        self.searcher = tSearcher(self.ui.txt_ruta.text(), self.ui.txt_consulta.text())
        self.searcher.updated.connect(self.add_row)
        self.searcher.start()

    pyqtSlot(list)
    def add_row(self, result):
        
        filename = QStandardItem(result[0])
        filename.setTextAlignment(Qt.AlignCenter)
        extension = QStandardItem(result[1])
        extension.setTextAlignment(Qt.AlignCenter)
        path = QStandardItem(result[2])
        path.setTextAlignment(Qt.AlignCenter)
        pattern = QStandardItem(result[3])
        pattern.setTextAlignment(Qt.AlignCenter)
        linea_nro = QStandardItem(str(result[4]))
        linea_nro.setTextAlignment(Qt.AlignCenter)
        self.model.appendRow([filename, extension, path, pattern, linea_nro])
        self.ui.tableSearch.setModel(self.model)
        self.ui.tableSearch.setModel(self.model)
        self.ui.tableSearch.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.ui.tableSearch.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.ui.tableSearch.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.ui.tableSearch.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
        self.ui.tableSearch.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeToContents)      


    def tableSearch(self):
        self.model = QStandardItemModel()
        self.model.setColumnCount(5)
        self.model.setRowCount(0)
        self.model.setHorizontalHeaderLabels(['Nombre Archivo', 'Extension', 'Ruta', 'Palabra', 'Linea #'])
        self.ui.tableSearch.setModel(self.model)
        self.ui.tableSearch.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.ui.tableSearch.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.ui.tableSearch.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.ui.tableSearch.horizontalHeader().setSectionResizeMode(3, QHeaderView.Stretch)
        self.ui.tableSearch.horizontalHeader().setSectionResizeMode(4, QHeaderView.Stretch)
        self.ui.tableSearch.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tableSearch.setDragDropOverwriteMode(False)
        self.ui.tableSearch.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.tableSearch.verticalHeader().setVisible(False)


class tSearcher(QThread):
    updated = pyqtSignal(list)
    def __init__(self, directory, pattern, parent=None):
        super(tSearcher, self).__init__(parent)
        self.directory = directory
        self.pattern = pattern

    def run(self):
        self.search(self.directory, self.pattern)            

    def search(self,directory,pattern):
        search = []
        _pattern = pattern
        pattern = re.compile(pattern, re.IGNORECASE)
        for path, _, files in os.walk(directory):
            for fn in files:
                if not fn.endswith('.dex'):
                    filepath = os.path.join(path, fn)
                    with open(filepath,encoding='latin1') as handle:
                        for lineno, line in enumerate(handle):
                            mo = pattern.search(line)
                            if mo:                        
                                #search.append([filepath,lineno, line.strip().replace(mo.group(),mo.group()) ])
                                filename = fn
                                ext = pathlib.Path(fn).suffix
                                linea = line.strip().replace(mo.group(),mo.group())
                                word = mo.group()                                
                                #search.append([filename, ext, filepath, word, lineno, linea, _pattern ])
                                search = [filename, ext, filepath, word, lineno + 1, linea, _pattern ]
                                self.updated.emit(search)                               
        return search 


if __name__ == '__main__':
    app = QApplication([])
    application = SuperGrep()
    application.show()
    sys.exit(app.exec())