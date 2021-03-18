import unittest
from lexer import Lexer
from testing_utils import assert_each_token

# testing correct lexeme classification of the Number token
class TestComment(unittest.TestCase):
    def test_single_line(self):
        source = "@! Hello, World!"

        # No tokens should be found since comments are skipped
        expected_token = []
        
        assert_each_token(self, source, expected_token)
    
    def test_multi_line(self):
        source = """
        @!! Hello, World! !@@
        String str = "Above line is skipped";
        """

        expected_token = [
            "('STRING', 'String')",
            "('ID', 'str')",
            "('OPERATOR', '=')",
            "('STRING_LITERAL', '\"Above line is skipped\"')",
            "('SEPARATOR', ';')"
        ]
        
        assert_each_token(self, source, expected_token)


if __name__ == '__main__':
    unittest.main()