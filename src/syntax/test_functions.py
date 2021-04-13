import unittest
from testing_utils import assert_syntax, assert_ast

# Testing correct syntax parsing of Number grammar


class TestFunctionGrammar(unittest.TestCase):
    def test_function_declaration(self) -> None:
        source_f = open('./given/function.ez', 'r')
        source = source_f.read()
        source_f.close()

        expected_f = open('./expected/function.txt', 'r')
        expected_syntax = expected_f.read()
        expected_f.close()

        expected_ast_f = open('./expected/function_ast.txt', 'r')
        expected_ast = expected_ast_f.read()
        expected_ast_f.close()

        assert_syntax(self, source, expected_syntax)
        assert_ast(self, source, expected_ast)


if __name__ == '__main__':
    unittest.main()
