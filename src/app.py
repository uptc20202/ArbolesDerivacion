import os
import sys
import typing
from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QDialog
from PyQt5.QtGui import QPixmap

from model.GrammarConfigure import GrammarConfigure
from model.Production import Production
from view.graphTree import create_graph,plot_graph

class gui_grammar(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("src/view/GramaticaFormal.ui", self)
        
        self.window = ProductionDialog()
        self.pop_up = PopUp()
        self.manager = GrammarConfigure()

        self.btnProducciones.clicked.connect(self.abrir_producciones)
        self.btnGenerateTree.clicked.connect(self.createAndAddGrammar)
        self.btnValidar.clicked.connect(self.validateWordOnGrammar)
        self.btnDetele.clicked.connect(self.clear_and_instantiate_manager)
 


    def abrir_producciones(self):
        self.window.exec_()

    def createAndAddGrammar(self):
        """Crear y agregar gramática."""
        grammarName = ""
        noTerminalSymbols = self.inputNoTerminal.toPlainText().split(",")
        sigma = self.inputAlfabeto.toPlainText().split(",")
        axiom = self.inputAxioma.toPlainText()
        productions = self.window.productionsList

        self.manager.create_grammar(grammarName, noTerminalSymbols, sigma, axiom, productions)

        create_graph(self.manager.get_general_root())
    
    def validateWordOnGrammar(self):
        try:
            word = self.inputPalabra.toPlainText()
            plot_graph(self.manager.get_particular_root(word))
        except Exception as e:
            self.pop_up.exec_()
            print("Error:", str(e))

    def clear_and_instantiate_manager(self):

        self.inputAlfabeto.clear()
        self.inputNoTerminal.clear()
        self.inputAxioma.clear()
        self.inputPalabra.clear()
        self.window.noTerminalSimbol.clear()
        self.window.productionInput.clear()

        self.window.productionsList = []
        self.manager = GrammarConfigure()
        
        self.window.labelProducciones.setText("V → Producción")


class ProductionDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("src/view/Producciones.ui", self)
        self.productionsList = []
        
        self.btnAdd.clicked.connect(self.add_production)

    def add_production(self): 
        no_terminal_symbol = self.noTerminalSimbol.toPlainText()
        production_input = self.productionInput.toPlainText()
        production = Production(no_terminal_symbol, production_input)
        self.productionsList.append(production)

        if self.labelProducciones:
            current_text = self.labelProducciones.text()
            new_text = f"{no_terminal_symbol} → {production_input}"
            self.labelProducciones.setText(new_text)

class PopUp(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("src/view/emergente.ui", self)
        
        image_name = 'src/view/x.png'
        pixmap = QPixmap(image_name)
        self.icono.setPixmap(pixmap)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = gui_grammar()
    GUI.show()
    sys.exit(app.exec_())

