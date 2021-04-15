import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'lexical')))
sys.path.append(os.path.abspath(os.path.join('..', 'utilities')))
from token_rules import tokens
from syntax_tree import SymbolType, NonTerminal, create_tree_node

# --------------------
# program
# --------------------
def p_program_nextLine(p):
    'program : nextLine'
    p[0] = p[1]

# --------------------
# nextLine
# --------------------
def p_nextLine(p):
    'nextLine : nextLinePrime'
    p[0] = p[1]

# --------------------
# nextLinePrime
# --------------------
def p_nextLinePrime_statement(p):
    'nextLinePrime : statement nextLinePrime'
    if p[2] == None:
        p[0] = p[1]
    else:
        p[0] = ('statement', p[1], p[2])

def p_nextLinePrime_empty(p):
    'nextLinePrime : '
    pass

# --------------------
# statement
# --------------------
def p_statement(p):
    '''statement : expression SEMICOLON
                 | ifStatement
                 | iterationStatement'''
    p[0] = p[1]


# --------------------
# iterationStatement
# --------------------
def p_iterationStatement(p):
    '''iterationStatement : WHILE LPAREN relationExpression RPAREN statementBody
                          | FOR LPAREN forExpression RPAREN statementBody'''
    if str(p[1]) == 'for':
        p[0] = ('forStatement', p[3], p[5])
    else:
        p[0] = ('whileStatement', p[3], p[5])

# --------------------
# forExpression
# --------------------
def p_forExpression(p):
    #'forExpression : LPAREN assignmentExpression SEMICOLON relationExpression SEMICOLON iterationExpression RPAREN'
    '''forExpression : expression SEMICOLON forExpression
                     | expression'''
    if len(p) >= 3:
        p[0] = ('forExpression', p[1], p[3])
    else:
        p[0] = p[1]
    
# --------------------
# ifStatement
# --------------------
def p_ifStatement(p):
    'ifStatement : IF LPAREN relationExpression RPAREN statementBody elifElseStatement'
    p[0] = ('ifStatement', p[3], p[5], p[6])

# --------------------
# statementBody
# --------------------
def p_statementBody(p):
    'statementBody : LCURLY statementBodyExpression RCURLY'
    p[0] = p[2]

# --------------------
# statementBodyExpression
# --------------------
def p_statementBodyExpression(p):
    '''statementBodyExpression : statement statementBodyExpression
                               | statement'''
    if len(p) >= 3: 
        p[0] = ('statementBodyExpression', p[1], p[2])
    else:
        p[0] = p[1]

def p_statementBodyExpression_empty(p):
    'statementBodyExpression : '
    pass

# --------------------
# elifElseStatement
# --------------------
def p_elifElseStatement(p):
    '''elifElseStatement : ELIF LPAREN relationExpression RPAREN statementBody elifElseStatement
                         | ELSE statementBody'''
    if str(p[1]) == 'ELIF':
        p[0] = ('elifElseStatement', p[3], p[5], p[6])
    else:
        p[0] = p[2]

def p_elifElseStatement_empty(p):
    'elifElseStatement : '
    pass

# --------------------
# expression
# --------------------
def p_expression(p):
    '''expression : assignmentExpression
                  | iterationExpression
                  | sumExpression
                  | multiplyExpression
                  | relationExpression'''
    p[0] = p[1]

# --------------------
# assignmentExpression
# --------------------
def p_assignmentExpression(p):
    '''assignmentExpression : variableDeclaration SET sumExpression
                            | ID SET sumExpression'''
    p[0] = ('assignmentExpression', p[2], p[1], p[3])

# --------------------
# iterationExpression
# --------------------
def p_iterationExpression(p):
    '''iterationExpression : assignmentExpression sumOperator multiplyExpression
                           | ID iterationOperator'''
    if len(p) >= 4:
        p[0] = ('iterationExpression', p[2], p[1], p[3])
    else:
        if str(p[2]) == '++':
            p[0] = ('iterationExpression', '+', p[1], 1)
        else:
            p[0] = ('iterationExpression', '-', p[1], 1)


# --------------------
# iterationOperator
# --------------------
def p_iterationOperator(p):
    '''iterationOperator : INCREMENT
                         | DECREMENT'''
    p[0] = p[1]

# --------------------
# relationExpression
# --------------------
def p_relationExpression(p):
    '''relationExpression : sumExpression relationOperator relationExpression
                          | sumExpression'''
    if len(p) >= 3:
        p[0] = ('relationExpression', p[2], p[1], p[3])
    else:
        p[0] = p[1]

# --------------------
# relationOperator
# --------------------
def p_relationOperator(p):
    '''relationOperator : EQUAL
                        | LESS_EQUAL
                        | GREATER_EQUAL
                        | NOT_EQUAL
                        | GREATER
                        | LESS'''
    p[0] = p[1]


# --------------------
# sumExpression
# --------------------
def p_sumExpression(p):
    '''sumExpression : multiplyExpression sumOperator sumExpression
                     | multiplyExpression'''
    if len(p) >= 3:
        p[0] = ('sumExpression', p[2], p[1], p[3])
    else:
        p[0] = p[1]

# --------------------
# multiplyExpression
# --------------------
def p_multiplyExpression(p):
    '''multiplyExpression : factor multiplyOperator multiplyExpression
                          | factor'''
    if len(p) >= 3:
        p[0] = ('multiplyExpression', p[2], p[1], p[3])
    else:
        p[0] = p[1]

# --------------------
# sumOperator
# --------------------
def p_sumOperator(p):
    '''sumOperator : PLUS
                   | MINUS'''
    p[0] = p[1]
    

# --------------------
# multiplyOperator
# --------------------
def p_multiplyOperator(p):
    '''multiplyOperator : MULTIPLY 
                        | DIVIDE
                        | MODULUS'''
    p[0] = p[1]

# --------------------
# mutable
# --------------------
def p_mutable(p):
    '''mutable : NUMBER_LITERAL
               | ID'''
    p[0] = p[1]

# --------------------
# immutable
# --------------------
def p_immutable(p):
    '''immutable : constant'''
    p[0] = p[1]

# --------------------
# constant
# --------------------
def p_constant(p):
    '''constant : TRUE 
                | FALSE'''
    p[0] = p[1]

# variableDeclaration
def p_variableDeclaration(p):
    '''variableDeclaration : NUMBER ID
                           | BOOLEAN ID
                           | STRING ID'''
    p[0] = p[2] # ignore the variable name

# factor
def p_factor(p):
    '''factor : mutable
              | immutable'''
    p[0] = p[1]
    
# error
def p_error(p):
    if p:
        print("Syntax error at token {0} -> {1}".format(p.type, p.value)) 