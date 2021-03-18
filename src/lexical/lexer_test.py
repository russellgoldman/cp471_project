import unittest
from typing import List, Set, Dict, Tuple, Optional
from lexer import Lexer

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
        
        l = Lexer()
        l.build(source)
        given_token = l.get_next_token()
        token_num = 0

        while given_token is not None:
            self.assertEqual(str(given_token), expected_token[token_num], 
                "Token {number} should be {expected}".format(number=token_num, expected=expected_token[token_num]))
                
            given_token = l.get_next_token()
            token_num = token_num + 1

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
        
        l = Lexer()
        l.build(source)
        given_token = l.get_next_token()
        token_num = 0

        while given_token is not None:
            self.assertEqual(str(given_token), expected_token[token_num], 
                "Token {number} should be {expected}".format(number=token_num, expected=expected_token[token_num]))
                
            given_token = l.get_next_token()
            token_num = token_num + 1


if __name__ == '__main__':
    unittest.main()