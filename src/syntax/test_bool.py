import unittest
from testing_utils import assert_syntax, assert_ast

# from parser import Parser

# Test lexeme classification for Boolean token


class TestBoolGrammer(unittest.TestCase):
    def test_bool_operators(self):
        source_f = open("./given/bool.ez", "r")
        source = source_f.read()
        source_f.close()

        expected_f = open("./expected/bool.txt", "r")
        expected_syntax = expected_f.read()
        expected_f.close()

        expected_ast_f = open("./expected/bool_ast.txt", "r")
        expected_ast = expected_ast_f.read()
        expected_ast_f.close()

        assert_syntax(self, source, expected_syntax)
        assert_ast(self, source, expected_ast)


if __name__ == '__main__':
    unittest.main()
