# Ref: https://ply.readthedocs.io/en/latest/ply.html
import sys, os
import ply.yacc as yacc
sys.path.append(os.path.abspath(os.path.join('..')))
import semantic.grammar_rules_ast as grammar_rules_ast
from lexer import Lexer

class Parser(object):
    # Build the parser using the grammar rules module
    def build(self, **kwargs):
        self.lexer = Lexer()
        self.lexer.build()
        self.parser = yacc.yacc(module=grammar_rules_ast, **kwargs)

    def parse(self, data, debug=False):
        return self.parser.parse(data, debug=debug, lexer = self.lexer)