class Grammar:
    def __init__(self, no_terminal_symbols, terminal_symbols, axiom_symbol):
        self.grammar_name = None
        self.no_terminal_symbols = no_terminal_symbols
        self.terminal_symbols = terminal_symbols
        self.axiom_symbol = axiom_symbol
        self.productions = []

    def get_grammar_name(self):
        return self.grammar_name

    def set_grammar_name(self, grammar_name):
        self.grammar_name = grammar_name

    def get_no_terminal_symbols(self):
        return self.no_terminal_symbols

    def set_no_terminal_symbols(self, no_terminal_symbols):
        self.no_terminal_symbols = no_terminal_symbols

    def get_terminal_symbols(self):
        return self.terminal_symbols

    def set_terminal_symbols(self, terminal_symbols):
        self.terminal_symbols = terminal_symbols

    def get_productions(self):
        return self.productions

    def set_productions(self, productions):
        self.productions = productions

    def get_axiom_symbol(self):
        return self.axiom_symbol

    def set_axiom_symbol(self, axiom_symbol):
        self.axiom_symbol = axiom_symbol
