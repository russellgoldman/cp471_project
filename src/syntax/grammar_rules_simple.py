import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'lexical')))
from token_rules import tokens

# program
def p_program_nextLine(p):
    'program : nextLine'
    p[0] = p[1]

# nextLine
def p_nextLine(p):
    'nextLine : nextLinePrime'
    p[0] = p[1]

# nextLinePrime
def p_nextLinePrime_statement(p):
    'nextLinePrime : statement nextLinePrime'
    p[0] = p[1]
    if p[2]: 
        p[0] + [p2]

def p_nextLinePrime_empty(p):
    'nextLinePrime : '
    pass

# statement
def p_statement_expression(p):
    'statement : expression SEMICOLON'
    p[0] = p[1] + p[2]

# expression
def p_expression_assignmentExpression(p):
    'expression : assignmentExpression'
    p[0] = p[1]

# assignmentExpression
def p_assignmentExpression(p):
    'assignmentExpression : variableDeclaration SET factor'
    p[0] = p[1] + p[2] + p[3]

# variableDeclaration
def p_variableDeclaration(p):
    'variableDeclaration : NUMBER ID'
    p[0] = p[1] + p[2]

# factor
def p_factor(p):
    'factor : NUMBER_LITERAL'
    p[0] = str(p[1])

# error
def p_error(p):
    if p:
        print("Syntax error at token {0} -> {1}".format(p.type, p.value)) 