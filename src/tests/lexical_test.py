import unittest
from typing import List, Set, Dict, Tuple, Optional

# testing correct lexeme classification of the Number token
class TestNumberToken(unittest.TestCase):
    s: str = "Number num = 10"

    def test_declaration(self) -> None:
        expected = '(Number)(id, num)(=)(10)(;)'
        given = ''

        # do the lexical stuff with given

        self.assertEqual(given, expected, "Should be something ...")

if __name__ == '__main__':
    unittest.main()