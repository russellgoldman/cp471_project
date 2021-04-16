import unittest
from testing_utils import assert_syntax

class TestStringGrammar(unittest.TestCase):
    def test_string_operations(self) -> None:
        source_f = open('./given/string_operations.ez', 'r')
        source = source_f.read()
        source_f.close()

        expected_f = open('./expected/string_operations.txt', 'r')
        expected = expected_f.read()
        expected_f.close()

        assert_syntax(self, source, expected)


if __name__ == '__main__':
    unittest.main()
