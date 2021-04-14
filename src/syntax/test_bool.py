import unittest
from testing_utils import assert_syntax

# from parser import Parser

# Test lexeme classification for Boolean token
class TestBoolGrammer(unittest.TestCase):
    def test_bool_operators(self):
        source_f = open("./given/bool.ez", "r")
        source = source_f.read()
        source_f.close()

        expected_f = open("./expected/bool.txt", "r")
        expected_syntax = expected_f.read()
        expected_f.close()

        assert_syntax(self, source, expected_syntax)


if __name__ == '__main__':
    unittest.main()
