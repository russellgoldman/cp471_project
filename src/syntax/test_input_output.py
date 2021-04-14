import unittest
from testing_utils import assert_syntax

# Testing correct syntax parsing of Number grammar


class TestInputOutputGrammar(unittest.TestCase):

    def test_input_declaration(self) -> None:
        source_f = open('./given/instream.ez', 'r')
        source = source_f.read()
        source_f.close()

        expected_f = open('./expected/input.txt', 'r')
        expected_syntax = expected_f.read()
        expected_f.close()

        assert_syntax(self, source, expected_syntax)

    '''def test_output_declaration(self) -> None:
        source_f = open('./given/output.ez', 'r')
        source = source_f.read()
        source_f.close()

        expected_f = open('./expected/output.txt', 'r')
        expected_syntax = expected_f.read()
        expected_f.close()

        assert_syntax(self, source, expected_syntax)'''


if __name__ == '__main__':
    unittest.main()
