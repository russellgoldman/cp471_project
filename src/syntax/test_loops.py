import unittest
from testing_utils import assert_syntax, assert_ast

class TestLoopGrammar(unittest.TestCase):
    def test_for_loop_declaration(self) -> None:
        source_f = open('./given/for_loop.ez', 'r')
        source = source_f.read()
        source_f.close()

        expected_f = open('./expected/for_loop.txt', 'r')
        expected_syntax = expected_f.read()
        expected_f.close()

        expected_ast_f = open('./expected/for_loop_ast.txt', 'r')
        expected_ast = expected_ast_f.read()
        expected_ast_f.close()

        assert_syntax(self, source, expected_syntax)
        assert_ast(self, source, expected_ast)

    def test_while_loop_declaration(self) -> None:
        source_f = open('./given/while_loop.ez', 'r')
        source = source_f.read()
        source_f.close()

        expected_f = open('./expected/while_loop.txt', 'r')
        expected_syntax = expected_f.read()
        expected_f.close()

        expected_ast_f = open('./expected/while_loop_ast.txt', 'r')
        expected_ast = expected_ast_f.read()
        expected_ast_f.close()

        assert_syntax(self, source, expected_syntax)
        assert_ast(self, source, expected_ast)


if __name__ == '__main__':
    unittest.main()
