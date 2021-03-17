import unittest
from typing import List, Set, Dict, Tuple, Optional
import ply.lex as lex

from lexical_ply import Lexer, tokenize

# testing correct lexeme classification of the Number token
class TestNumberToken(unittest.TestCase):
    s: str = "Number num = 10"

    def test_declaration(self) -> None:
        expected = '(Number)(id, num)(=)(10)(;)'
        tokens = tokenize(str)

        given = ''.join(["({str})".format(str=str(tok)) for tok in tokens]) 

        self.assertEqual(given, expected, "Should be something ...")

if __name__ == '__main__':
    unittest.main()