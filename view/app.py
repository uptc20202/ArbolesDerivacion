import sys
import typing
from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QDialog


class gui_grammar(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("view/GramaticaFormal.ui", self)
        self.window = ProductionDialog()
        self.btnProducciones.clicked.connect(self.abrir_producciones)

    def abrir_producciones(self):
        self.window.exec_()

class ProductionDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("view/Producciones.ui", self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = gui_grammar()
    GUI.show()
    sys.exit(app.exec_())

