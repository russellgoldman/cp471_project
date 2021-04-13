import unittest
from testing_utils import assert_syntax, assert_ast

# Testing correct syntax parsing of Number grammar


class TestInputOutputGrammar(unittest.TestCase):

    def test_input_declaration(self) -> None:
        source_f = open('./given/ipnput.ez', 'r')
        source = source_f.read()
        source_f.close()

        expected_f = open('./expected/input.txt', 'r')
        expected_syntax = expected_f.read()
        expected_f.close()

        expected_ast_f = open('./expected/input_ast.txt', 'r')
        expected_ast = expected_ast_f.read()
        expected_ast_f.close()

        assert_syntax(self, source, expected_syntax)
        assert_ast(self, source, expected_ast)

    def test_output_declaration(self) -> None:
        source_f = open('./given/output.ez', 'r')
        source = source_f.read()
        source_f.close()

        expected_f = open('./expected/output.txt', 'r')
        expected_syntax = expected_f.read()
        expected_f.close()

        expected_ast_f = open('./expected/output_ast.txt', 'r')
        expected_ast = expected_ast_f.read()
        expected_ast_f.close()

        assert_syntax(self, source, expected_syntax)
        assert_ast(self, source, expected_ast)


if __name__ == '__main__':
    unittest.main()
