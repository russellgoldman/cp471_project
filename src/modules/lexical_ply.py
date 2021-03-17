# Lexical Analyzer implemented using ply (lex and yacc)
# Ref: https://ply.readthedocs.io/en/latest/ply.html
import ply.lex as lex
import ply.yacc as yacc

class Lexer(object):
    reserved = {
        'if' : 'IF',
        'elif' : 'ELIF',
        'else' : 'ELSE',
        'for' : 'FOR',
        'while' : 'WHILE',
        'this' : 'THIS',
        'return' : 'RETURN',
        'Import' : 'IMPORT',
        'Number' : 'NUMBER',
        'String' : 'STRING',
        'Boolean' : 'BOOLEAN',
        'Function' : 'FUNCTION',
        'Object' : 'OBJECT',
        'print' : 'PRINT',
        'out' : 'OUT',
        'input' : 'INPUT',
        'in' : 'IN'
    }
    tokens = [
        'ID',
        'KEYWORD',
        'OPERATOR',
        'NUMBER_LITERAL',
        'SEPARATOR'
    ] + list(reserved.values())
    
    #--------------------
    # Token Definitions
    #--------------------
    # Tokens can be defined as strings or as functions using regex
    def t_ID(self, t):
        r'([A-Za-z]|_)([A-Za-z]|[0-9]|_)*'
        # Look up symbol type in symbol table
        # t.value = (t.value, symbol_lookup(t.value))
        # Check if ID is a reserved word
        t.type = self.reserved.get(t.value, 'ID')
        return t

    def t_KEYWORD(self, t):
        r'if|elif|else|for|while|this|Number|String|Boolean|Function|Object|return|Import|print|input|in|out'
        return t

    def t_OPERATOR(self, t):
        r'==|<=|>=|!=|>|<|=|\+|-|\*|\*\*|/|%'
        return t

    def t_NUMBER_LITERAL(self, t):
        r'[0-9]+|([0-9]+.[0-9]+)'
        t.value = int(t.value)
        return t

    def t_SEPARATOR(self, t):
        r'\(|\)|{|}|\[|\]|;|,|\#|@|\->|>>|<<|\|.'
        return t

    # Error handling rule
    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    # Build the lexer
    def build(self,**kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    # Test it output
    def get_tokens(self, source):
        self.lexer.input(source)
        self.tokens = []
        tok = self.get_next_token()
        while tok != None:
            self.tokens.append(tok)
            tok = self.get_next_token()
        return self.tokens
    
    def get_next_token(self):
        tok = self.lexer.token()
        if not tok:
            return None
        return tok

def tokenize(source):
    lexer = Lexer()
    lexer.build()
    return lexer.get_tokens(source)