import unittest
from lexer import Lexer
from testing_utils import assert_each_token
# testing correct lexeme classification of the Number token


class TestStringToken(unittest.TestCase):
    def test_for_loop(self):
        source = "Function add = (Number num1, Number num2) -> (Number) { return (num1 + num2); }"
        expected_token = [
            "('FUNCTION', 'Function')",
            "('ID', 'add')",
            "('OPERATOR', '=')",
            "('SEPARATOR', '(')",
            "('NUMBER', 'Number')",
            "('ID', 'num1')",
            "('SEPARATOR', ',')",
            "('NUMBER', 'Number')",
            "('ID', 'num2')",
            "('SEPARATOR', ')')",
            # Lexer finds ("OPERATOR,'-'") instead of ('SEPARATOR', '->')
            "('SEPARATOR', '->')",
            "('SEPARATOR', '(')",
            "('NUMBER', 'Number')",
            "('SEPARATOR', ')')",
            "('SEPARATOR', '{')",
            "('RETURN', 'return')",
            "('SEPARATOR', '(')",
            "('ID', 'num1')",
            "('OPERATOR', '+')",
            "('ID', 'num2')",
            "('SEPARATOR', ')')",
            "('SEPARATOR', ';')",
            "('SEPARATOR', '}')",

        ]
        assert_each_token(self, source, expected_token)


if __name__ == '__main__':
    unittest.main()
