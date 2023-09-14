import unittest
from model.Production import Production
from model.Axiom import Axiom
from model.Cheker import Checker
from model.CreateNode import CreateNode
from model.Grammar import Grammar
from model.WordModel import WordModel
from model.GrammarConfigure import GrammarConfigure

class TestGrammar(unittest.TestCase):
    def setUp(self):
        self.grammar_config = GrammarConfigure()
        grammar_name = "Test Grammar"
        no_terminal_symbols = ["a","b"]
        terminal_symbols = ["S"]
        axiom_symbol = "S"
        productions = [Production("S", "aSb"), Production("S", "ab")]
        self.grammar_config.create_grammar(grammar_name, no_terminal_symbols, terminal_symbols, axiom_symbol, productions)

    def test_create_grammar(self):
        self.assertIsNotNone(self.grammar_config.grammar)

    def test_generate_general_tree(self):
        self.assertIsNotNone(self.grammar_config.general_root)

    def test_add_branch(self):
        # Asegurarse de que el número de hijos del nodo raíz es correcto
        self.assertEqual(len(self.grammar_config.general_root.get_children_symbol()), 2)

    def test_add_words_to_father(self):
        # Asegurarse de que las palabras se añaden correctamente al nodo padre
        for child in self.grammar_config.general_root.get_children_symbol():
            self.assertIn(child.get_symbol().get_symbol(), ["ab", "ab"])

    def test_format_word(self):
        # Asegurarse de que la palabra se formatea correctamente
        symbols = ["S"]
        production = "aSb"
        symbol_position = 0
        formatted_word = self.grammar_config.format_word(symbols, production, symbol_position)
        self.assertEqual(formatted_word, "aSb")

    def test_is_no_terminal(self):
        # Asegurarse de que el método devuelve True para los símbolos no terminales y False para los símbolos terminales
        self.assertTrue(self.grammar_config.is_no_terminal("S"))
        self.assertFalse(self.grammar_config.is_no_terminal("a"))

    def test_search_production(self):
        # Asegurarse de que el método devuelve las producciones correctas para un símbolo no terminal dado
        productions = self.grammar_config.search_production("S")
        self.assertEqual(productions, ["aSb", "ab"])

if __name__ == '__main__':
    unittest.main()
