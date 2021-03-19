import unittest
from lexer import Lexer
from testing_utils import assert_each_token

# Test lexeme classification for conditional tokens
class TestConditionalToken(unittest.TestCase):
    def test_if_statement(self):
        source = "if (bool == True) { } else { }"

        expected_token = [
            "('IF', 'if')",
            "('SEPARATOR', '(')",
            "('ID', 'bool')",
            "('OPERATOR', '==')",
            "('TRUE', 'True')",
            "('SEPARATOR', ')')",
            "('SEPARATOR', '{')",
            "('SEPARATOR', '}')",
            "('ELSE', 'else')",
            "('SEPARATOR', '{')",
            "('SEPARATOR', '}')",
        ]
        assert_each_token(self, source, expected_token)

    def test_elif_statement(self):
        source = "if (bool == True) { } elif ( bool == False) { }"

        expected_token = [
            "('IF', 'if')",
            "('SEPARATOR', '(')",
            "('ID', 'bool')",
            "('OPERATOR', '==')",
            "('TRUE', 'True')",
            "('SEPARATOR', ')')",
            "('SEPARATOR', '{')",
            "('SEPARATOR', '}')",
            "('ELIF', 'elif')",
            "('SEPARATOR', '(')",
            "('ID', 'bool')",
            "('OPERATOR', '==')",
            "('FALSE', 'False')",
            "('SEPARATOR', ')')",
            "('SEPARATOR', '{')",
            "('SEPARATOR', '}')",
        ]

        assert_each_token(self, source, expected_token)


if __name__ == '__main__':
    unittest.main()
