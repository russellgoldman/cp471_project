import unittest
from testing_utils import assert_syntax

# Testing correct syntax parsing of Number grammar
class TestNumberGrammar(unittest.TestCase):
    def test_number_declaration(self) -> None:
        source_f = open('./given/number.ez', 'r')
        source = source_f.read()
        source_f.close()

        expected_f = open('./expected/number.txt', 'r')
        expected_syntax = expected_f.read()
        expected_f.close()
        
        assert_syntax(self, source, expected_syntax)

    def test_number_assignment(self) -> None:
        source_f = open('./given/assignment.ez', 'r')
        source = source_f.read()
        source_f.close()

        expected_f = open('./expected/assignment.txt', 'r')
        expected_syntax = expected_f.read()
        expected_f.close()
        
        assert_syntax(self, source, expected_syntax)
if __name__ == '__main__':
    unittest.main()