import unittest
from ez_parser import Parser

def assert_syntax(self, source, expected_syntax, debug=False):
    p = Parser()
    p.build()
    given_syntax = p.parse(source, debug)

    # check that the syntax is correct
    self.assertEqual(str(given_syntax), expected_syntax)