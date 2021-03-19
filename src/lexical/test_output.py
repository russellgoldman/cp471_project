import unittest
from lexer import Lexer
from testing_utils import assert_each_token

# Test lexeme classification for output tokens
class TestOutputToken(unittest.TestCase):
    def test_output_function(self):
        source = "print(str);"

        expected_token = [
            "('PRINT', 'print')",
            "('SEPARATOR', '(')",
            "('ID', 'str')",
            "('SEPARATOR', ')')",
            "('SEPARATOR', ';')"
        ]
        
        assert_each_token(self, source, expected_token)

    def test_output_stream(self):
        source = "out << str << \" and more\";"

        expected_token = [
            "('OUT', 'out')",
            "('OPERATOR', '<<')",
            "('ID', 'str')",
            "('OPERATOR', '<<')",
            "('STRING_LITERAL', '\" and more\"')",
            "('SEPARATOR', ';')"
        ]
        
        assert_each_token(self, source, expected_token)


if __name__ == '__main__':
    unittest.main()