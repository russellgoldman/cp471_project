import unittest
from lexer import Lexer
from testing_utils import assert_each_token

# Test lexeme classification for input tokens
class TestInputToken(unittest.TestCase):
    def test_input_function(self):
        source = "String str = input();"

        expected_token = [
            "('STRING', 'String')",
            "('ID', 'str')",
            "('SET', '=')",
            "('INPUT', 'input')",
            "('LPAREN', '(')",
            "('RPAREN', ')')",
            "('SEMICOLON', ';')"
        ]
        
        assert_each_token(self, source, expected_token)
    
    def test_input_stream(self):
        source = "in >> str;"

        expected_token = [
            "('IN', 'in')",
            "('IN_PIPE', '>>')",
            "('ID', 'str')",
            "('SEMICOLON', ';')"
        ]
        
        assert_each_token(self, source, expected_token)


if __name__ == '__main__':
    unittest.main()