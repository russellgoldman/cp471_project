import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'lexical')))
print(sys.path)
from token_rules import tokens

# program
def p_program_nextLine(p):
    'program : nextLine SEMICOLON'
    p[0] = p[1]

def p_program_empty(p):
    'program : '
    p[0] = None

# nextLine
def p_nextLine_number(p):
    'nextLine : NUMBER_LITERAL'
    p[0] = p[1]

def p_nextLine_id(p):
    'nextLine : ID'
    p[0] = p[1]

def p_nextLine_equals(p):
    'nextLine : SET'
    p[0] = p[1]