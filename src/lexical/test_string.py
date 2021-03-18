import unittest
from lexer import Lexer
from testing_utils import assert_each_token

# testing correct lexeme classification of the Number token


class TestStringToken(unittest.TestCase):
    def test_string_declaration(self):
        source = "String str = \"Hello, World!\";"

        expected_token = [
            "('STRING', 'String')",
            "('ID', 'str')",
            "('OPERATOR', '=')",
            "('STRING_LITERAL', '\"Hello, World!\"')",
            "('SEPARATOR', ';')"
        ]
        
        assert_each_token(self, source, expected_token)

    def test_string_operators(self):
        source = "String str3 = str1 + str2;"

        expected_token = [
            "('STRING', 'String')",
            "('ID', 'str3')",
            "('OPERATOR', '=')",
            "('ID', 'str1')",
            "('OPERATOR', '+')",
            "('ID', 'str2')",
            "('SEPARATOR', ';')"
        ]
        
        assert_each_token(self, source, expected_token)


if __name__ == '__main__':
    unittest.main()
