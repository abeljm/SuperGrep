from PyQt5.QtCore import pyqtSignal, QThread
import re
import os
import pathlib

class Searcher(QThread):
    updated = pyqtSignal(list)
    def __init__(self, directory, pattern, parent=None):
        super(Searcher, self).__init__(parent)
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