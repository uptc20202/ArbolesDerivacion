from model.Axiom import Axiom
from model.Cheker import Checker
from model.CreateNode import CreateNode
from model.Grammar import Grammar
from model.WordModel import WordModel


class GrammarConfigure:
    def __init__(self):
        self.grammar = None
        self.general_root = None
        self.checker = None

    def create_grammar(self, grammar_name, no_terminal_symbols, terminal_symbols, axiom_symbol, productions):
        self.grammar = Grammar(self.change_to_list(no_terminal_symbols), self.change_to_list(terminal_symbols), axiom_symbol)
        self.grammar.set_grammar_name(grammar_name)
        self.grammar.set_productions(productions)
        self.generate_general_tree()
        self.checker = Checker(self.grammar)

    def change_to_list(self, _list):
        return list(_list)

    def generate_general_tree(self):
        self.general_root = CreateNode(Axiom(self.grammar.get_axiom_symbol()))
        self.add_branch(self.general_root, 0)

    def add_branch(self, father, level):
        if level < 5:
            symbols = father.get_symbol().get_symbol()
            for i in range(len(symbols)):
                symbol = symbols[i]
                if self.is_no_terminal(symbol):
                    self.add_words_to_father(father, symbols, i, symbol)
                    break
            level += 1
            children_symbol = father.get_children_symbol()
            for child_symbol in children_symbol:
                self.add_branch(child_symbol, level)

    def add_words_to_father(self, father, symbols, i, symbol):
        print(symbol)
        symbols_productions = self.search_production(str(symbol))##Esto era str(symbol)
        for string in symbols_productions:
            father.add_child(CreateNode(WordModel(self.format_word(symbols, string, i))))

    def format_word(self, symbols, production, symbol_position):
        word = ""
        for i in range(len(symbols)):
            symbol = symbols[i]
            if i == symbol_position:
                word += production
            else:
                word += symbol
        return word

    def is_no_terminal(self, character):
        return character in self.grammar.get_no_terminal_symbols()

    def search_production(self, no_terminal_symbol):
        symbols_productions = []
        productions = self.grammar.get_productions()
        for production in productions:
            if no_terminal_symbol == production.get_no_terminal_symbol():
                symbols_productions.append(production.get_production())
        return symbols_productions

    def print_grammar(self):
        print("Simbolos no terminales-------")
        symbol_list_one = self.grammar.get_no_terminal_symbols()
        for string in symbol_list_one:
            print(string)
        print("Simbolos terminales--------")
        symbol_list_two = self.grammar.get_terminal_symbols()
        for string in symbol_list_two:
            print(string)
        print("Axioma---------")
        print(self.grammar.get_axiom_symbol())
        productions = self.grammar.get_productions()
        for production in productions:
            print(production)

    def print_tree(self):
        self.print_node(self.general_root, 1, -1)

    def print_node(self, node, level, father_id):
        print(node, " - FatherId=", father_id, " - level=", level)
        level += 1
        for child in node.get_children_symbol():
            self.print_node(child, level, node.get_id())

    def get_general_root(self):
        return self.general_root

    def get_particular_root(self, word):
        return self.checker.get_tree_word(word)

    def get_grammar_name(self):
        return self.grammar.get_grammar_name()
