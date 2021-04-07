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
    'statement : expression SEMICOLON'
    p[0] = create_tree_node(NonTerminal.STATEMENT, [
        (p[1], SymbolType.NONTERMINAL),
        (p[2], SymbolType.TERMINAL)
    ])
    # p[0] = p[1] + p[2]

# expression
def p_expression_assignmentExpression(p):
    'expression : assignmentExpression'
    p[0] = create_tree_node(NonTerminal.EXPRESSION, [
        (p[1], SymbolType.NONTERMINAL)
    ])
    # p[0] = p[1]

# assignmentExpression
def p_assignmentExpression(p):
    'assignmentExpression : variableDeclaration SET factor'
    p[0] = create_tree_node(NonTerminal.ASSIGNMENT_EXPRESSION, [
        (p[1], SymbolType.NONTERMINAL),
        (p[2], SymbolType.TERMINAL),
        (p[3], SymbolType.NONTERMINAL),
    ])
    # p[0] = p[1] + p[2] + p[3]

# variableDeclaration
def p_variableDeclaration(p):
    'variableDeclaration : NUMBER ID'
    p[0] = create_tree_node(NonTerminal.VARIABLE_DECLARATION, [
        (p[1], SymbolType.TERMINAL),
        (p[2], SymbolType.TERMINAL)
    ])
    # p[0] = p[1] + p[2]

# factor
def p_factor(p):
    'factor : NUMBER_LITERAL'
    p[0] = create_tree_node(NonTerminal.FACTOR, [
        (p[1], SymbolType.TERMINAL)
    ])
    # p[0] = str(p[1])

# error
def p_error(p):
    if p:
        print("Syntax error at token {0} -> {1}".format(p.type, p.value)) 