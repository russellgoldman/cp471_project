import unittest
from lexer import Lexer
from testing_utils import assert_each_token

# Test lexeme classification for function tokens
class TestFunctionToken(unittest.TestCase):
    def test_function_declaration(self):
        source = "Function add = (Number num1, Number num2) -> (Number) { return (num1 + num2); }"
        expected_token = [
            "('FUNCTION', 'Function')",
            "('ID', 'add')",
            "('OPERATOR', '=')",
            "('LPAREN', '(')",
            "('NUMBER', 'Number')",
            "('ID', 'num1')",
            "('SEPARATOR', ',')",
            "('NUMBER', 'Number')",
            "('ID', 'num2')",
            "('RPAREN', ')')",
            "('RETURNS', '->')",
            "('LPAREN', '(')",
            "('NUMBER', 'Number')",
            "('RPAREN', ')')",
            "('LCURLY', '{')",
            "('RETURN', 'return')",
            "('LPAREN', '(')",
            "('ID', 'num1')",
            "('PLUS', '+')",
            "('ID', 'num2')",
            "('RPAREN', ')')",
            "('SEMICOLON', ';')",
            "('RCURLY', '}')",

        ]
        assert_each_token(self, source, expected_token)


if __name__ == '__main__':
    unittest.main()
