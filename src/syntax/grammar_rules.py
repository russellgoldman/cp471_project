import sys, os
sys.path.append(os.path.abspath(os.path.join('..')))
from lexical.token_rules import tokens
from utilities.syntax_tree import SymbolType, NonTerminal, create_tree_node

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

# --------------------
# statement
# --------------------
def p_statement(p):
    '''statement : expression SEMICOLON
                 | ifStatement
                 | iterationStatement
                 | inputStatement SEMICOLON
                 | outputStatement SEMICOLON'''
    if len(p) == 3:
        p[0] = create_tree_node(NonTerminal.STATEMENT, [
            (p[1], SymbolType.NONTERMINAL),
            (p[2], SymbolType.TERMINAL)
        ])
    else:
        p[0] = create_tree_node(NonTerminal.STATEMENT, [
            (p[1], SymbolType.NONTERMINAL)
        ])
    # p[0] = p[1] + p[2]


# --------------------
# statementBody
# --------------------
def p_iterationStatement(p):
    '''iterationStatement : WHILE LPAREN relationExpression RPAREN statementBody
                          | FOR LPAREN assignmentExpression SEMICOLON relationExpression SEMICOLON iterationExpression RPAREN statementBody'''
    if len(p) >= 7:
        p[0] = create_tree_node(NonTerminal.ITERATION_STATEMENT, [
                (p[1], SymbolType.TERMINAL),
                (p[2], SymbolType.TERMINAL),
                (p[3], SymbolType.NONTERMINAL),
                (p[4], SymbolType.TERMINAL),
                (p[5], SymbolType.NONTERMINAL),
                (p[6], SymbolType.TERMINAL),
                (p[7], SymbolType.NONTERMINAL),
                (p[8], SymbolType.TERMINAL),
                (p[9], SymbolType.NONTERMINAL),
        ])
    else:
        p[0] = create_tree_node(NonTerminal.ITERATION_STATEMENT, [
                (p[1], SymbolType.TERMINAL),
                (p[2], SymbolType.TERMINAL),
                (p[3], SymbolType.NONTERMINAL),
                (p[4], SymbolType.TERMINAL),
                (p[5], SymbolType.NONTERMINAL),
        ])

# --------------------
# outputStatement
# --------------------
def p_outputStatement(p):
    '''outputStatement : outFunction'''
    p[0] = create_tree_node(NonTerminal.OUTPUT_STATEMENT, [
        (p[1], SymbolType.NONTERMINAL)
    ])

# --------------------
# ifStatement
# --------------------
def p_ifStatement(p):
    'ifStatement : IF LPAREN relationExpression RPAREN statementBody elifElseStatement'
    p[0] = create_tree_node(NonTerminal.IF_STATEMENT, [
        (p[1], SymbolType.TERMINAL),
        (p[2], SymbolType.TERMINAL),
        (p[3], SymbolType.NONTERMINAL),
        (p[4], SymbolType.TERMINAL),
        (p[5], SymbolType.NONTERMINAL),
        (p[6], SymbolType.NONTERMINAL)
    ])

# --------------------
# statementBody
# --------------------
def p_statementBody(p):
    'statementBody : LCURLY statementBodyExpression RCURLY'
    if p[2] == None:
        p[0] = create_tree_node(NonTerminal.STATEMENT_BODY, [
            (p[1], SymbolType.TERMINAL),
            (p[3], SymbolType.TERMINAL)
        ])
    else:
        p[0] = create_tree_node(NonTerminal.STATEMENT_BODY, [
            (p[1], SymbolType.TERMINAL),
            (p[2], SymbolType.NONTERMINAL),
            (p[3], SymbolType.TERMINAL)
        ])

# --------------------
# statementBodyExpression
# --------------------
def p_statementBodyExpression(p):
    '''statementBodyExpression : statement
                               | expression'''
    p[0] = create_tree_node(NonTerminal.STATEMENT_BODY_EXPRESSION, [
        (p[1], SymbolType.NONTERMINAL)
    ])

def p_statementBodyExpression_empty(p):
    'statementBodyExpression : '
    pass

# --------------------
# elifElseStatement
# --------------------
def p_elifElseStatement(p):
    '''elifElseStatement : ELIF LPAREN relationExpression RPAREN statementBody elifElseStatement
                         | ELSE statementBody'''
    if len(p) >= 4:
        if p[6] == None:
            p[0] = create_tree_node(NonTerminal.ELIF_ELSE_STATEMENT, [
                (p[1], SymbolType.TERMINAL),
                (p[2], SymbolType.TERMINAL),
                (p[3], SymbolType.NONTERMINAL),
                (p[4], SymbolType.TERMINAL),
                (p[5], SymbolType.NONTERMINAL)
            ])
        else:
            p[0] = create_tree_node(NonTerminal.ELIF_ELSE_STATEMENT, [
                (p[1], SymbolType.TERMINAL),
                (p[2], SymbolType.TERMINAL),
                (p[3], SymbolType.NONTERMINAL),
                (p[4], SymbolType.TERMINAL),
                (p[5], SymbolType.NONTERMINAL),
                (p[6], SymbolType.NONTERMINAL),
            ])
    else:
        p[0] = create_tree_node(NonTerminal.ELIF_ELSE_STATEMENT, [
            (p[1], SymbolType.TERMINAL),
            (p[2], SymbolType.NONTERMINAL)
        ])

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
                  | multiplyExpression'''
    p[0] = create_tree_node(NonTerminal.EXPRESSION, [
        (p[1], SymbolType.NONTERMINAL)
    ])
    # p[0] = p[1]

# --------------------
# assignmentExpression
# --------------------
def p_assignmentExpression(p):
    'assignmentExpression : variableDeclaration SET sumExpression'
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
    '''iterationExpression : ID SET ID sumOperator multiplyExpression
                           | ID iterationOperator'''
    if len(p) >= 4:
        p[0] = create_tree_node(NonTerminal.ITERATION_EXPRESSION, [
            (p[1], SymbolType.NONTERMINAL),
            (p[2], SymbolType.TERMINAL),
            (p[3], SymbolType.NONTERMINAL),
            (p[4], SymbolType.NONTERMINAL),
            (p[5], SymbolType.NONTERMINAL),
        ])
    else:
        p[0] = create_tree_node(NonTerminal.ITERATION_EXPRESSION, [
            (p[1], SymbolType.NONTERMINAL),
            (p[2], SymbolType.NONTERMINAL)
        ])

# --------------------
# iterationOperator
# --------------------
def p_iterationOperator(p):
    '''iterationOperator : INCREMENT
                         | DECREMENT'''
    p[0] = create_tree_node(NonTerminal.ITERATION_OPERATOR, [
        (p[1], SymbolType.TERMINAL)
    ])

# --------------------
# relationExpression
# --------------------
def p_relationExpression(p):
    'relationExpression : sumExpression relationExpressionPrime'
    if p[2] == None:
        p[0] = create_tree_node(NonTerminal.RELATION_EXPRESSION, [
            (p[1], SymbolType.NONTERMINAL),
        ])
    else:
        p[0] = create_tree_node(NonTerminal.RELATION_EXPRESSION, [
            (p[1], SymbolType.NONTERMINAL),
            (p[2], SymbolType.NONTERMINAL),
        ])

# --------------------
# relationExpressionPrime
# --------------------
def p_relationExpressionPrime(p):
    'relationExpressionPrime : relationOperator sumExpression relationExpressionPrime'
    if p[3] == None:
        p[0] = create_tree_node(NonTerminal.RELATION_EXPRESSION_PRIME, [
            (p[1], SymbolType.NONTERMINAL),
            (p[2], SymbolType.NONTERMINAL)
        ])
    else:
        p[0] = create_tree_node(NonTerminal.RELATION_EXPRESSION_PRIME, [
        (p[1], SymbolType.NONTERMINAL),
        (p[2], SymbolType.NONTERMINAL),
        (p[3], SymbolType.NONTERMINAL)
    ])

def p_relationExpressionPrime_empty(p):
    'relationExpressionPrime : '
    pass

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
    p[0] = create_tree_node(NonTerminal.RELATION_OPERATOR, [
        (p[1], SymbolType.TERMINAL)
    ])

# --------------------
# sumExpression
# --------------------
def p_sumExpression(p):
    'sumExpression : multiplyExpression sumExpressionPrime'
    if p[2] == None:
        p[0] = create_tree_node(NonTerminal.SUM_EXPRESSION, [
            (p[1], SymbolType.NONTERMINAL),
        ])
    else:
        p[0] = create_tree_node(NonTerminal.SUM_EXPRESSION, [
            (p[1], SymbolType.NONTERMINAL),
            (p[2], SymbolType.NONTERMINAL),
        ])

# --------------------
# sumExpressionPrime
# --------------------
def p_sumExpressionPrime(p):
    'sumExpressionPrime : sumOperator multiplyExpression sumExpressionPrime'
    if p[3] == None:
        p[0] = create_tree_node(NonTerminal.SUM_EXPRESSION_PRIME, [
            (p[1], SymbolType.NONTERMINAL),
            (p[2], SymbolType.NONTERMINAL),
        ])
    else:
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
    if p[2] == None:
        p[0] = create_tree_node(NonTerminal.MULTIPLY_EXPRESSION, [
            (p[1], SymbolType.NONTERMINAL),
        ])
    else:
        p[0] = create_tree_node(NonTerminal.MULTIPLY_EXPRESSION, [
            (p[1], SymbolType.NONTERMINAL),
            (p[2], SymbolType.NONTERMINAL),
        ])

# --------------------
# multiplyExpressionPrime
# --------------------
def p_multiplyExpressionPrime(p):
    'multiplyExpressionPrime : multiplyOperator factor multiplyExpressionPrime'
    if p[3] == None:
        p[0] = create_tree_node(NonTerminal.MULTIPLY_EXPRESSION_PRIME, [
            (p[1], SymbolType.NONTERMINAL),
            (p[2], SymbolType.NONTERMINAL),
        ])
    else:
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
# multiplyOperator
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
# outStream
# --------------------
def p_outFunction(p):
    '''outFunction : PRINT LPAREN ID RPAREN
                   | PRINT LPAREN STRING_LITERAL RPAREN'''
    p[0] = create_tree_node(NonTerminal.OUT_FUNCTION, [
        (p[1], SymbolType.TERMINAL),
        (p[2], SymbolType.TERMINAL),
        (p[3], SymbolType.NONTERMINAL),
        (p[4], SymbolType.TERMINAL)
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