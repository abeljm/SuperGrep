from PyQt5.QtCore import pyqtSignal, QThread
import re
import os
import pathlib

class Searcher(QThread):
    updated = pyqtSignal(list)
    files = pyqtSignal(str)
    finished = pyqtSignal()
    def __init__(self, directory, pattern, ex_ruta, black_list, parent=None):
        super(Searcher, self).__init__(parent)
        self.directory = directory
        self.pattern = pattern
        self.ex_ruta = ex_ruta
        self.black_list = black_list

    def run(self):
        self.search(self.directory, self.pattern, self.ex_ruta, self.black_list)            

    def search(self, _directory, pattern, _ex_ruta, black_list):
        search = []
        _pattern = pattern
        pattern = re.compile(pattern, re.IGNORECASE)
        directory = pathlib.Path(_directory)
        ex_ruta = pathlib.Path(_ex_ruta)
        
        for path, _, files in os.walk(directory):            
            if os.name == 'nt':
                path = os.path.abspath(path)
            for fn in files:
                self.files.emit(fn)
                if fn not in black_list: # if not fn.endswith('.dex'):                
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
        self.finished.emit()