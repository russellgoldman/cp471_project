import unittest
from lexer import Lexer

def assert_each_token(self, source, expected_token, print_token=False):
    l = Lexer()
    l.build()
    l.input(source)
    given_token = l.token()
    token_num = 0

    while given_token is not None:
        # check if number of identified tokens exceeds the correct amount
        if token_num > len(expected_token) - 1:
            self.assertEqual(token_num, len(expected_token) - 1, "Identified tokens exceed correct amount")

        # check that the current token is correct
        self.assertEqual(str((given_token.type, given_token.value)), expected_token[token_num],
                         "Token {number} should be {expected}".format(number=token_num, expected=expected_token[token_num]))

        if print_token == True:
            print(str(given_token))
        given_token = l.token()
        token_num = token_num + 1

    # check if number of identified tokens is less than the correct amount
    self.assertEqual(token_num, len(expected_token), "Identified tokens are less than the correct amount")

    