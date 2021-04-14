import unittest
from testing_utils import assert_syntax

class TestConditionalGrammar(unittest.TestCase):
    def test_conditional_declaration(self) -> None:
        source_f = open('./given/conditional.ez', 'r')
        source = source_f.read()
        source_f.close()

        expected_f = open('./expected/conditional.txt', 'r')
        expected = expected_f.read()
        expected_f.close()

        assert_syntax(self, source, expected)


if __name__ == '__main__':
    unittest.main()
