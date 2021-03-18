# Ref: https://ply.readthedocs.io/en/latest/ply.html
import ply.lex as lex
import token_rules

class Lexer(object):
    # Build the lexer using the token rules module
    def build(self, data, **kwargs):
        self.lexer = lex.lex(module=token_rules, **kwargs)
        self.lexer.input(data)

    # Get the next token
    def get_next_token(self):
        tok = self.lexer.token()

        if not tok:
            return None
        return (tok.type, tok.value)