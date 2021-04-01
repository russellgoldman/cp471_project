# Ref: https://ply.readthedocs.io/en/latest/ply.html
import ply.yacc as yacc
import grammar_rules_simple
from lexer import Lexer

class Parser(object):
    # Build the parser using the grammar rules module
    def build(self, data, **kwargs):
        self.lexer = Lexer().build(data)
        self.parser = yacc.yacc(module=grammar_rules_simple, **kwargs)

        s = input(data)
        result = self.parser.parse(s, lexer = self.lexer)
        

p = Parser()
p.build('Number num = 10;')