

class Axiom:
    def __init__(self, symbol):
        self.symbol = symbol

    def getPathImage(self):
        return "src/img/axiomNode.png"

    def get_symbol(self):
        return self.symbol

    def __str__(self):
        return self.symbol
