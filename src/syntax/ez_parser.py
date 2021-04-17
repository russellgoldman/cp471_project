# Ref: https://ply.readthedocs.io/en/latest/ply.html
import sys, os

sys.path.append(os.path.abspath(os.path.join('..')))
import ply.yacc as yacc
import grammar_rules
from lexical.lexer import Lexer

class Parser(object):
    # Build the parser using the grammar rules module
    def build(self, **kwargs):
        self.lexer = Lexer()
        self.lexer.build()
        self.parser = yacc.yacc(module=grammar_rules, **kwargs)

    def parse(self, data, debug=False):
        return self.parser.parse(data, debug=debug, lexer = self.lexer)