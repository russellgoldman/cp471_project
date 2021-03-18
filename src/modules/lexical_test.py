import unittest
from typing import List, Set, Dict, Tuple, Optional
from lexical import Lexer

# testing correct lexeme classification of the Number token
class TestNumberToken(unittest.TestCase):
    test_str: str = "Number num = 10;"

    def test_declaration(self) -> None:
        expected_token = [
            "('NUMBER', 'Number')",
            "('ID', 'num')",
            "('OPERATOR', '=')",
            "('NUMBER_LITERAL', 10)",
            "('SEPARATOR', ';')"
        ]
        l = Lexer()
        l.build(self.test_str)
        given_token = l.get_next_token()
        token_num = 0
        while given_token is not None:
            self.assertEqual(str(given_token), expected_token[token_num], "Should be something ...")
            given_token = l.get_next_token()
            token_num = token_num + 1

if __name__ == '__main__':
    unittest.main()