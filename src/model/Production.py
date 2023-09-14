class Production:

    def __init__(self, no_terminal_symbol, production):
        self.no_terminal_symbol = no_terminal_symbol
        self.production = production

    def get_no_terminal_symbol(self):
        return str(self.no_terminal_symbol)

    def set_no_terminal_symbol(self, no_terminal_symbol):
        self.no_terminal_symbol = no_terminal_symbol

    def get_production(self):
        return self.production

    def set_production(self, production):
        self.production = production

    def __str__(self):
        return "Production [noTerminalSymbol=" + self.no_terminal_symbol + ", production=" + self.production + "]"