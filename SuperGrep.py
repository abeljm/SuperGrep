from PyQt5.QtWidgets import QMainWindow, QApplication, QHeaderView, QFileDialog, QTableWidgetItem, QAbstractItemView
from PyQt5.QtCore import Qt, pyqtSlot, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap
from functools import partial
from interface.main import Ui_MainWindow
from utils.Searcher import Searcher
import sys
import html

class SuperGrep(QMainWindow):
    def __init__(self):
        super(SuperGrep, self).__init__()
        self.ui = Ui_MainWindow()        
        self.ui.setupUi(self)
        self.tableSearch()
        self.setWindowIcon(QIcon("resources/lupa.png"))
        self.ui.btn_rutaExaminar.setIcon(QIcon(QPixmap("resources/carpeta.png")))
        self.ui.btn_rutaExaminar.setLayoutDirection(Qt.RightToLeft)

        self.ui.btn_excluirExaminar.setIcon(QIcon(QPixmap("resources/carpeta.png")))
        self.ui.btn_excluirExaminar.setLayoutDirection(Qt.RightToLeft)

        self.ui.btn_buscar.setIcon(QIcon(QPixmap("resources/encontrar.png")))
        self.ui.btn_buscar.setLayoutDirection(Qt.RightToLeft)

        self.ui.btn_rutaExaminar.clicked.connect(partial(self.browse, self.ui.txt_ruta))
        self.ui.btn_excluirExaminar.clicked.connect(partial(self.browse, self.ui.txt_excluirRuta))
        self.ui.btn_buscar.clicked.connect(self.scan)
        self.ui.tableSearch.currentCellChanged.connect(self.dataRow)
        self.result_search = list()

    def browse(self,edit):
        fileName = QFileDialog.getExistingDirectory(self, 'Select directory')
        if fileName:
            edit.setText(fileName)

    def scan(self):
        ruta = self.ui.txt_ruta.text()
        self.searcher = Searcher(ruta, self.ui.txt_consulta.text())
        self.searcher.updated.connect(self.add_row)
        self.searcher.start()

    def dataRow(self, row, column):

        # Sumary
        self.ui.tedit_sumary.clear()
        r_files = []
        contador = 0
        self.ui.tedit_sumary.appendHtml("Resultados de la busqueda:  ")
        
        self.ui.tedit_sumary.appendHtml("<br>Palabra: <b>" + self.ui.txt_consulta.text() + " <b>")        

        for j in range(len(self.result_search)):
            if self.ui.txt_consulta.text() == self.result_search[j][6]:
                if self.result_search[j][0] not in r_files:
                    r_files.append(self.result_search[j][0])
                contador += 1         

        self.ui.tedit_sumary.appendHtml("Cantidad coincidencias: " + str(contador))
        self.ui.tedit_sumary.appendHtml("Cantidad Archivos: " + str(len(r_files)) + "<br>")

        for r_file in r_files:
            self.ui.tedit_sumary.appendHtml(r_file)
        r_files.clear()

        # hints
        self.ui.tedit_hints.clear()
        self.ui.tedit_hints.appendHtml("<b>Archivo:</b> " + self.result_search[row][0])
        self.ui.tedit_hints.appendHtml("<b>Extension:</b> " + self.result_search[row][1])
        self.ui.tedit_hints.appendHtml("<b>Ruta:</b> " + self.result_search[row][2])
        self.ui.tedit_hints.appendHtml("<b>Palabra encontrada:</b> " + self.result_search[row][3])
        self.ui.tedit_hints.appendHtml("<b>Palabra buscada:</b> " + self.result_search[row][6])
        self.ui.tedit_hints.appendHtml("<b>Nro Linea:</b> " + str(self.result_search[row][4]))
        linea = html.escape(self.result_search[row][5])
        linea = linea.replace(self.result_search[row][3], "<font color=\"red\">" + self.result_search[row][3] + "</font>")
        self.ui.tedit_hints.appendHtml("<b>Linea:</b> <br><br>" + linea)

        # preview
        self.ui.tedit_preview.clear()
        text = open(self.result_search[row][2], encoding='latin1').read()
        self.ui.tedit_preview.insertPlainText(text)

    pyqtSlot(list)
    def add_row(self, result):
        self.result_search.append(result)        
        rowPosition = self.ui.tableSearch.rowCount()
        self.ui.tableSearch.insertRow(rowPosition)
        
        item1 = QTableWidgetItem(result[0])
        item2 = QTableWidgetItem(result[1])
        item3 = QTableWidgetItem(result[2])
        item4 = QTableWidgetItem(result[3])
        item5 = QTableWidgetItem(str(result[4]))

        item1.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter | Qt.AlignCenter)
        item2.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter | Qt.AlignCenter)
        item3.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter | Qt.AlignCenter)
        item4.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter | Qt.AlignCenter)
        item5.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter | Qt.AlignCenter)

        self.ui.tableSearch.setItem(rowPosition, 0, QTableWidgetItem(item1))  # item1
        self.ui.tableSearch.setItem(rowPosition, 1, QTableWidgetItem(item2))  # item2
        self.ui.tableSearch.setItem(rowPosition, 2, QTableWidgetItem(item3))  # item3
        self.ui.tableSearch.setItem(rowPosition, 3, QTableWidgetItem(item4))  # item4
        self.ui.tableSearch.setItem(rowPosition, 4, QTableWidgetItem(item5))  # item5

    def tableSearch(self):
        # Deshabilitar edición
        self.ui.tableSearch.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # Deshabilitar el comportamiento de arrastrar y soltar
        self.ui.tableSearch.setDragDropOverwriteMode(False)
        # Seleccionar toda la fila
        self.ui.tableSearch.setSelectionBehavior(QAbstractItemView.SelectRows)
        # Establecer el número de columnas
        self.ui.tableSearch.setColumnCount(5)
        # Establecer el número de filas
        self.ui.tableSearch.setRowCount(0)
        # Alineación del texto del encabezado
        self.ui.tableSearch.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter | Qt.AlignVCenter | Qt.AlignCenter)
        # Ocultar encabezado vertical
        self.ui.tableSearch.verticalHeader().setVisible(False)
        nombreColumnas = ('Nombre Archivo', 'Extension', 'Ruta', 'Palabra', 'Linea #')
        # Establecer las etiquetas de encabezado horizontal usando etiquetas
        self.ui.tableSearch.setHorizontalHeaderLabels(nombreColumnas)
        # todo los headers de la tabla se ponen del mismo tamaño
        self.ui.tableSearch.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


if __name__ == '__main__':
    app = QApplication([])
    application = SuperGrep()
    application.show()
    sys.exit(app.exec())