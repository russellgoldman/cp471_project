import unittest
from lexer import Lexer
from testing_utils import assert_each_token

# Test lexeme classification for loop tokens
class TestLoopToken(unittest.TestCase):
    def test_for_loop(self):
        source = "for(Number i=0; i<10; i++){ }"
        expected_token = [
            "('FOR', 'for')",
            "('SEPARATOR', '(')",
            "('NUMBER', 'Number')",
            "('ID', 'i')",
            "('OPERATOR', '=')",
            "('NUMBER_LITERAL', 0)",
            "('SEPARATOR', ';')",
            "('ID', 'i')",
            "('OPERATOR', '<')",
            "('NUMBER_LITERAL', 10)",
            "('SEPARATOR', ';')",
            "('ID', 'i')",
            "('OPERATOR', '++')",
            "('SEPARATOR', ')')",
            "('SEPARATOR', '{')",
            "('SEPARATOR', '}')",
        ]
        assert_each_token(self, source, expected_token)

    def test_while_loop(self):
        source = "while(bool == True) { }"

        expected_token = [
            "('WHILE', 'while')",
            "('SEPARATOR', '(')",
            "('ID', 'bool')",
            "('OPERATOR', '==')",
            "('TRUE', 'True')",
            "('SEPARATOR', ')')",
            "('SEPARATOR', '{')",
            "('SEPARATOR', '}')",
        ]

        assert_each_token(self, source, expected_token)


if __name__ == '__main__':
    unittest.main()
