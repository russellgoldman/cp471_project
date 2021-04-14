import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'lexical')))
sys.path.append(os.path.abspath(os.path.join('..', 'utilities')))
from token_rules import tokens
from syntax_tree import SymbolType, NonTerminal, create_tree_node

# program
def p_program_nextLine(p):
    'program : nextLine'
    p[0] = create_tree_node(NonTerminal.PROGRAM, [
        (p[1], SymbolType.NONTERMINAL)
    ])
    # p[0] = p[1]

# nextLine
def p_nextLine(p):
    'nextLine : nextLinePrime'
    p[0] = create_tree_node(NonTerminal.NEXT_LINE, [
        (p[1], SymbolType.NONTERMINAL)
    ])
    # p[0] = p[1]

# nextLinePrime
def p_nextLinePrime_statement(p):
    'nextLinePrime : statement nextLinePrime'
    if p[2]:
        p[0] = create_tree_node(NonTerminal.NEXT_LINE_PRIME, [
            (p[1], SymbolType.NONTERMINAL),
            (p[2], SymbolType.NONTERMINAL)
        ])
    else:
        p[0] = create_tree_node(NonTerminal.NEXT_LINE_PRIME, [
            (p[1], SymbolType.NONTERMINAL)
        ])

    # p[0] = p[1]
    # if p[2]: 
    #     p[0] += p[2]

def p_nextLinePrime_empty(p):
    'nextLinePrime : '
    pass

# statement
def p_statement_expression(p):
    '''statement : expression SEMICOLON
                 | inputStatement SEMICOLON'''
    p[0] = create_tree_node(NonTerminal.STATEMENT, [
        (p[1], SymbolType.NONTERMINAL),
        (p[2], SymbolType.TERMINAL)
    ])
    # p[0] = p[1] + p[2]

# --------------------
# expression
# --------------------
def p_expression(p):
    '''expression : assignmentExpression
                  | iterationExpression
                  | sumExpression
                  | multiplyExpression'''
    p[0] = create_tree_node(NonTerminal.EXPRESSION, [
        (p[1], SymbolType.NONTERMINAL)
    ])
    # p[0] = p[1]

# --------------------
# assignmentExpression
# --------------------
def p_assignmentExpression(p):
    'assignmentExpression : variableDeclaration SET factor'
    p[0] = create_tree_node(NonTerminal.ASSIGNMENT_EXPRESSION, [
        (p[1], SymbolType.NONTERMINAL),
        (p[2], SymbolType.TERMINAL),
        (p[3], SymbolType.NONTERMINAL),
    ])
    # p[0] = p[1] + p[2] + p[3]

# --------------------
# iterationExpression
# --------------------
def p_iterationExpression(p):
    '''iterationExpression : ID SET ID sumOperator multiplyExpression'''
    p[0] = create_tree_node(NonTerminal.ITERATION_EXPRESSION, [
        (p[1], SymbolType.NONTERMINAL),
        (p[2], SymbolType.TERMINAL),
        (p[3], SymbolType.NONTERMINAL),
        (p[4], SymbolType.NONTERMINAL),
        (p[5], SymbolType.NONTERMINAL),
    ])

# --------------------
# sumExpression
# --------------------
def p_sumExpression(p):
    'sumExpression : multiplyExpression sumExpressionPrime'
    p[0] = create_tree_node(NonTerminal.SUM_EXPRESSION, [
        (p[1], SymbolType.NONTERMINAL),
        (p[2], SymbolType.NONTERMINAL),
    ])

# --------------------
# sumExpressionPrime
# --------------------
def p_sumExpressionPrime(p):
    'sumExpressionPrime : sumOperator multiplyExpression sumExpressionPrime'
    p[0] = create_tree_node(NonTerminal.SUM_EXPRESSION_PRIME, [
        (p[1], SymbolType.NONTERMINAL),
        (p[2], SymbolType.NONTERMINAL),
        (p[3], SymbolType.NONTERMINAL),
    ])

def p_sumExpressionPrime_empty(p):
    'sumExpressionPrime : '
    pass

# --------------------
# multiplyExpression
# --------------------
def p_multiplyExpression(p):
    'multiplyExpression : factor multiplyExpressionPrime'
    p[0] = create_tree_node(NonTerminal.MULTIPLY_EXPRESSION, [
        (p[1], SymbolType.NONTERMINAL),
        (p[2], SymbolType.NONTERMINAL),
    ])

# --------------------
# multiplyExpressionPrime
# --------------------
def p_multiplyExpressionPrime(p):
    'multiplyExpressionPrime : multiplyOperator factor multiplyExpressionPrime'
    p[0] = create_tree_node(NonTerminal.MULTIPLY_EXPRESSION_PRIME, [
        (p[1], SymbolType.NONTERMINAL),
        (p[2], SymbolType.NONTERMINAL),
        (p[3], SymbolType.NONTERMINAL),
    ])

def p_multiplyExpressionPrime_empty(p):
    'multiplyExpressionPrime : '
    pass

# --------------------
# sumOperator
# --------------------
def p_sumOperator(p):
    '''sumOperator : PLUS
                   | MINUS'''
    p[0] = create_tree_node(NonTerminal.SUM_OPERATOR, [
        (p[1], SymbolType.TERMINAL)
    ])

# --------------------
# sumOperator
# --------------------
def p_multiplyOperator(p):
    '''multiplyOperator : MULTIPLY 
                        | DIVIDE
                        | MODULUS'''
    p[0] = create_tree_node(NonTerminal.MULTIPLY_OPERATOR, [
        (p[1], SymbolType.TERMINAL)
    ])

# --------------------
# inputStatement
# --------------------
def p_inputStatement(p):
    '''inputStatement : inStream'''
    p[0] = create_tree_node(NonTerminal.INPUT_STATEMENT, [
        (p[1], SymbolType.NONTERMINAL)
    ])

# --------------------
# inStream
# --------------------
def p_inStream(p):
    'inStream : IN IN_PIPE ID'
    p[0] = create_tree_node(NonTerminal.IN_STREAM, [
        (p[1], SymbolType.TERMINAL),
        (p[2], SymbolType.TERMINAL),
        (p[3], SymbolType.NONTERMINAL)
    ])

# --------------------
# mutable
# --------------------
def p_mutable(p):
    '''mutable : NUMBER_LITERAL
               | inputStatement
               | ID'''
    p[0] = create_tree_node(NonTerminal.MUTABLE, [
        (p[1], SymbolType.TERMINAL)
    ])

# --------------------
# immutable
# --------------------
def p_immutable(p):
    '''immutable : constant'''
    p[0] = create_tree_node(NonTerminal.IMMUTABLE, [
        (p[1], SymbolType.NONTERMINAL)
    ])

# --------------------
# constant
# --------------------
def p_constant(p):
    '''constant : TRUE 
                | FALSE'''
    p[0] = create_tree_node(NonTerminal.CONSTANT, [
        (p[1], SymbolType.TERMINAL)
    ])

# variableDeclaration
def p_variableDeclaration(p):
    '''variableDeclaration : NUMBER ID
                           | BOOLEAN ID
                           | STRING ID'''
    p[0] = create_tree_node(NonTerminal.VARIABLE_DECLARATION, [
        (p[1], SymbolType.TERMINAL),
        (p[2], SymbolType.TERMINAL)
    ])
    # p[0] = p[1] + p[2]

# factor
def p_factor(p):
    '''factor : mutable
              | immutable'''
    p[0] = create_tree_node(NonTerminal.FACTOR, [
        (p[1], SymbolType.NONTERMINAL)
    ])
    # p[0] = str(p[1])

# error
def p_error(p):
    if p:
        print("Syntax error at token {0} -> {1}".format(p.type, p.value)) 