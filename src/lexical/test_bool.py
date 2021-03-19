import unittest
from lexer import Lexer
from testing_utils import assert_each_token

# Test lexeme classification for Boolean token
class TestBoolToken(unittest.TestCase):
    def test_bool_operators(self):
        source = "Boolean bool = True;"

        expected_token = [
            "('BOOLEAN', 'Boolean')",
            "('ID', 'bool')",
            "('OPERATOR', '=')",
            "('TRUE', 'True')",
            "('SEPARATOR', ';')"
        ]

        assert_each_token(self, source, expected_token)


if __name__ == '__main__':
    unittest.main()
