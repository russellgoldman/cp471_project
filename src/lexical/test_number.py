import unittest
from typing import List, Set, Dict, Tuple, Optional
from lexer import Lexer
from testing_utils import assert_each_token

# testing correct lexeme classification of the Number token
class TestNumberToken(unittest.TestCase):
    def test_number_declaration(self) -> None:
        source: str = "Number num = 10;"

        expected_token = [
            "('NUMBER', 'Number')",
            "('ID', 'num')",
            "('OPERATOR', '=')",
            "('NUMBER_LITERAL', 10)",
            "('SEPARATOR', ';')"
        ]
        
        assert_each_token(self, source, expected_token)

    def test_number_operators(self) -> None:
        source: str = "num = num + 2 * 3;"

        expected_token = [
            "('ID', 'num')",
            "('OPERATOR', '=')",
            "('ID', 'num')",
            "('OPERATOR', '+')",
            "('NUMBER_LITERAL', 2)",
            "('OPERATOR', '*')",
            "('NUMBER_LITERAL', 3)",
            "('SEPARATOR', ';')"
        ]
        
        assert_each_token(self, source, expected_token)

    def test_undefined_number(self) -> None:
        source: str = "Number num;"

        expected_token = [
            "('NUMBER', 'Number')",
            "('ID', 'num')",
            "('SEPARATOR', ';')"
        ]

        assert_each_token(self, source, expected_token)

if __name__ == '__main__':
    unittest.main()