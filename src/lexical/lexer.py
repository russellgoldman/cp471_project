# Ref: https://ply.readthedocs.io/en/latest/ply.html
import sys, os
import ply.lex as lex
sys.path.append(os.path.abspath(os.path.join('./lexical')))
import token_rules as token_rules

class Lexer(object):
    # Build the lexer using the token rules module
    def build(self, **kwargs):
        self.lexer = lex.lex(module=token_rules, **kwargs)
    
    # Sets the input
    def input(self, data):
        self.lexer.input(str(data))

    # Returns full token
    def token(self):
        tok = self.lexer.token()
        return tok