import unittest
from testing_utils import assert_syntax

class TestOutputGrammar(unittest.TestCase):
    def test_output_function(self) -> None:
        source_f = open('./given/output.ez', 'r')
        source = source_f.read()
        source_f.close()

        expected_f = open('./expected/output.txt', 'r')
        expected = expected_f.read()
        expected_f.close()

        assert_syntax(self, source, expected)


if __name__ == '__main__':
    unittest.main()
