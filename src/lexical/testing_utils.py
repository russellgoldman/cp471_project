import unittest
from lexer import Lexer

def assert_each_token(self, source, expected_token):
    l = Lexer()
    l.build(source)
    given_token = l.get_next_token()
    token_num = 0

    while given_token is not None:
        self.assertEqual(str(given_token), expected_token[token_num],
                        "Token {number} should be {expected}".format(number=token_num, expected=expected_token[token_num]))

        given_token = l.get_next_token()
        token_num = token_num + 1