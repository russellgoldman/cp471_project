import unittest
from lexer import Lexer
from testing_utils import assert_each_token

# Test lexeme classification for conditional tokens
class TestConditionalToken(unittest.TestCase):
    def test_if_statement(self):
        source = """
        if (bool == True) {
            @! Something
        } else {
            @! Something else
        }
        """

        expected_token = [
            "('IF', 'if')",
            "('LPAREN', '(')",
            "('ID', 'bool')",
            "('OPERATOR', '==')",
            "('TRUE', 'True')",
            "('RPAREN', ')')",
            "('LCURLY', '{')",
            "('RCURLY', '}')",
            "('ELSE', 'else')",
            "('LCURLY', '{')",
            "('RCURLY', '}')",
        ]
        assert_each_token(self, source, expected_token)

    def test_elif_statement(self):
        source = """
        if (bool == True) {
            @! Something
        } elif ( bool == False) {
            @! Something else
        }
        """

        expected_token = [
            "('IF', 'if')",
            "('LPAREN', '(')",
            "('ID', 'bool')",
            "('OPERATOR', '==')",
            "('TRUE', 'True')",
            "('RPAREN', ')')",
            "('LCURLY', '{')",
            "('RCURLY', '}')",
            "('ELIF', 'elif')",
            "('LPAREN', '(')",
            "('ID', 'bool')",
            "('OPERATOR', '==')",
            "('FALSE', 'False')",
            "('RPAREN', ')')",
            "('LCURLY', '{')",
            "('RCURLY', '}')",
        ]

        assert_each_token(self, source, expected_token)


if __name__ == '__main__':
    unittest.main()
