class CreateNode:
    sequential = 0

    def __init__(self, symbol):
        self.id = CreateNode.sequential
        CreateNode.sequential += 1
        self.symbol = symbol
        self.childrenSymbol = []

    def get_id(self):
        return self.id

    def get_symbol(self):
        return self.symbol

    def set_symbol(self, symbol):
        self.symbol = symbol

    def get_children_symbol(self):
        return self.childrenSymbol

    def add_child(self, child):
        self.childrenSymbol.append(child)

    def __str__(self):
        return " symbol=" + self.symbol.get_symbol()
