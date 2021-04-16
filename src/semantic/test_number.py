import unittest
from testing_utils import assert_ast

# Testing correct syntax parsing of Number grammar
class TestNumberGrammar(unittest.TestCase):
    def test_number_declaration(self) -> None:
        source_f = open('./given/number.ez', 'r')
        source = source_f.read()
        source_f.close()

        expected_f = open('./expected/number.txt', 'r')
        expected = expected_f.read()
        expected_f.close()

        assert_ast(self, source, expected)

if __name__ == '__main__':
    unittest.main()