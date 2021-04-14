import unittest
from testing_utils import assert_syntax

class TestInputOutputGrammar(unittest.TestCase):
    def test_input_stream(self) -> None:
        source_f = open('./given/input_stream.ez', 'r')
        source = source_f.read()
        source_f.close()

        expected_f = open('./expected/input_stream.txt', 'r')
        expected = expected_f.read()
        expected_f.close()

        assert_syntax(self, source, expected)


if __name__ == '__main__':
    unittest.main()
