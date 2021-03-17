# Lexical Analyzer implemented using ply (lex and yacc)
# Ref: https://ply.readthedocs.io/en/latest/ply.html
import ply.lex as lex
import ply.yacc as yacc

class Lexical:
    def __init__(self, source):
        self.source = source
        
    #--------------------
    # Token Names
    #--------------------
    # All tokens in the language
    # Must have a defn
    tokens = (
        'ID',
        'PLUS',
        'MINUS',
        'TIMES',
        'DIVIDE',
        'LPAREN',
        'RPAREN',
    )

    #--------------------
    # Reserved Names / Keywords
    #--------------------
    # These words cannot be used as an ID
    # --> See ID defn
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

    #--------------------
    # Token Definitions
    #--------------------
    # Tokens can be defined as strings or as functions using regex
    def t_ID(self, t):
        r'([A-Za-z]|_)([A-Za-z]|[0-9]|_)*'
        # Look up in symbol table
        # t.value = (t.value, symbol_lookup(t.value))
        # Check if ID is a reserved word
        t.type = reserved.get(t.value, 'ID')
        return t