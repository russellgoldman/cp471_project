import unittest
from lexer import Lexer
from testing_utils import assert_each_token

# Test lexeme classification for loop tokens
class TestLoopToken(unittest.TestCase):
    def test_for_loop(self):
        source = "for (Number i=0; i<10; i++) { }"
        expected_token = [
            "('FOR', 'for')",
            "('LPAREN', '(')",
            "('NUMBER', 'Number')",
            "('ID', 'i')",
            "('OPERATOR', '=')",
            "('NUMBER_LITERAL', 0)",
            "('SEMICOLON', ';')",
            "('ID', 'i')",
            "('LESS', '<')",
            "('NUMBER_LITERAL', 10)",
            "('SEMICOLON', ';')",
            "('ID', 'i')",
            "('INCREMENT', '++')",
            "('RPAREN', ')')",
            "('LCURLY', '{')",
            "('RCURLY', '}')",
        ]
        assert_each_token(self, source, expected_token)

    def test_while_loop(self):
        source = "while (bool == True) { }"

        expected_token = [
            "('WHILE', 'while')",
            "('LPAREN', '(')",
            "('ID', 'bool')",
            "('EQUAL', '==')",
            "('TRUE', 'True')",
            "('RPAREN', ')')",
            "('LCURLY', '{')",
            "('RCURLY', '}')",
        ]

        assert_each_token(self, source, expected_token)


if __name__ == '__main__':
    unittest.main()
