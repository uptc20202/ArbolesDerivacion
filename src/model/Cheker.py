from model.Axiom import Axiom
from model.NoTerminal import NoTerminal
from model.Node import Node
from model.Terminal import Terminal
from model.Production import Production

class Checker:
    def __init__(self, grammar):
        self.grammar = grammar

    def get_tree_word(self, word):
        return self.get_tree(self.check_word(word))

    def get_tree(self, language):
        if language is not None:
            tree = Node(Axiom(language.get_symbol().get_no_terminal_symbol()))
            next_node = tree
            while language is not None:
                no_terminal_symbol = NoTerminal(language.get_symbol().get_no_terminal_symbol())
                terminal_symbol = Terminal(language.get_symbol().get_production())
                next_node.set_left(Node(no_terminal_symbol))
                next_node.set_right(Node(terminal_symbol))
                next_node = next_node.get_right()
                language = language.get_right()
                print("@Cheker @get_tree tree",tree)
            return tree
        return None

    def check_word(self, word):
        language = Node(Production("",""))
        actual_non_terminal = None
        first_non_terminal = self.grammar.get_axiom_symbol()
        actual_productions = self.get_productions(first_non_terminal)
        for i in range(len(word)):
            if i + 1 == len(word):
                production = self.get_terminal_production(" " + word[i], actual_productions, word[i])
                if production is not None:
                    language.add_to_bottom(Node(production))
                    print("@Cheker @check_word languaje",language)
                    return language
            else:
                print("@Cheker @check_word if false")
                production1 = self.get_non_terminal_productions(actual_non_terminal, actual_productions, word[i])
                actual_non_terminal = actual_productions[-1].get_production()[-1]
                actual_productions.extend(self.get_productions(actual_non_terminal))
                language.add_to_bottom(Node(production1))
        print("Palabra no existe")
        return None

    def get_productions(self, non_terminal_symbol):
        return [p for p in self.grammar.get_productions() if p.get_no_terminal_symbol() == non_terminal_symbol]

    def get_non_terminal_productions(self, symbol, productions, letter):
        for p in productions:
            production = p.get_production()
            if not production.isupper():
                if p.get_production()[0] == letter:
                    return p
        return None

    def get_terminal_production(self, symbol, productions, letter):
        for p in productions:
            production = p.get_production()
            if not production.isupper():
                if p.get_production()[0] == letter and len(p.get_production()) == 1:
                    return p
        return None
