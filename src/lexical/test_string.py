import unittest
from lexer import Lexer

# testing correct lexeme classification of the Number token


class TestStringToken(unittest.TestCase):
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

        l = Lexer()
        l.build(source)
        given_token = l.get_next_token()
        token_num = 0

        while given_token is not None:
            self.assertEqual(str(given_token), expected_token[token_num],
                             "Token {number} should be {expected}".format(number=token_num, expected=expected_token[token_num]))

            given_token = l.get_next_token()
            token_num = token_num + 1


if __name__ == '__main__':
    unittest.main()
