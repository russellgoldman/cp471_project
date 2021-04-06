import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'lexical')))
print(sys.path)
import token_rules

# program
def p_program_nextLine(p):
    'program : nextLine'
    p[0] = p[1]

def p_program_empty(p):
    'program : '
    p[0] = None


# nextLine
def p_nextLine(p):
    'nextLine: nextLinePrime'
    p[0] = p[1]


# nextLinePrime
def p_nextLinePrime_statement(p):
    'nextLinePrime : statement nextLinePrime'
    p[0] = p[1] + p[2]

def p_nextLinePrime_functionDefinition(p):
    'nextLinePrime : functionDefinition nextLinePrime'
    p[0] = p[1] + p[2]

def p_nextLinePrime_comment(p):
    'nextLinePrime : comment nextLinePrime'
    p[0] = p[1] + p[2]    

def p_nextLinePrime_import(p):
    'nextLinePrime : import nextLinePrime'
    p[0] = p[1] + p[2]

def p_nextLinePrime_empty(p):
    'nextLinePrime : '
    p[0] = None


# statement
def p_statement_expression(p):
    'statement : expression'
    p[0] = p[1]

def p_statement_ifStatement(p):
    'statement : ifStatement'
    p[0] = p[1]

def p_statement_iterationStatement(p):
    'statement : iterationStatement'
    p[0] = p[1]

def p_statement_returnStatement(p):
    'statement : returnStatement'
    p[0] = p[1]


# expression
def p_expression_iterationExpression(p):
    'expression : iterationExpression'
    p[0] = p[1]

def p_expression_assignmentExpression(p):
    'expression : assignmentExpression'
    p[0] = p[1]

def p_expression_relationExpression(p):
    'expression : relationExpression'
    p[0] = p[1]

def p_expression_sumExpression(p):
    'expression : sumExpression'
    p[0] = p[1]

def p_expression_multiplyExpression(p):
    'expression : multiplyExpression'
    p[0] = p[1]


# returnStatement
def p_returnStatement_return(p):
    'returnStatement : return returnExpression'
    p[0] = + p[2]


# returnExpression
def p_returnExpression_relationExpression(p):
    'returnExpression : relationExpression'
    p[0] = p[1]

def p_returnExpression_sumExpression(p):
    'returnExpression : sumExpression'
    p[0] = p[1]

def p_returnExpression_multiplyExpression(p):
    'returnExpression : multiplyExpression'
    p[0] = p[1]


# ifStatement
def p_ifStatement(p):
    'ifStatement : if LPARAMS relationExpression RPARAMS statementBody elifElseStatement'
    p[0] = p[5]


# elifElseStatement
def p_elifElseStatement_elif(p):
    'elifElseStatement : elif LPARAMS relationExpression RPARAMS statementBody elifElseStatement'
    p[0] = p[5]

def p_elifElseStatement_else(p):
    'elifElseStatement : else statementBody'
    p[0] = p[2]

def p_elifElseStatement_empty(p):
    'elifElseStatement : '
    p[0] = None


# statementBody
def p_statementBody(p):
    'statementBody : LCURLY statementBodyExpression RCURLY'
    p[0] = p[2]


# statementBodyExpression
def p_statementBodyExpression_statement(p):
    'statementBodyExpression : statement'
    p[0] = p[1]

def p_statementBodyExpression_expression(p):
    'statementBodyExpression : expression'
    p[0] = p[1]

def p_statementBodyExpression_outputStatement(p):
    'statementBodyExpression : outputStatement'
    p[0] = p[1]


# iterationStatement
def p_iterationStatement_while(p):
    'iterationStatement : while LPARAMS relationExpression statementBody'
    p[0] = p[1]

def p_iterationStatement_for(p):
    'iterationStatement : for LPARAMS variableDeclaration SET NUMBER_LITERAL SEMICOLON relationExpression SEMICOLON iterationExpression RPARAMS statementBody'

# iterationExpression
def p_iterationExpression_set(p):
    'iterationExpression : ID SET ID operator multiplyExpression'

def p_iterationExpression_incDec(p):
    'iterationExpression : ID iterationOperator'


# iterationOperator
def p_iterationOperator_increment(p):
    'iterationOperator : INCREMENT'
    p[0] = p[0] + 1

def p_iterationOperator_decrement(p):
    'iterationOperator : DECREMENT'
    p[0] = p[0] - 1


# assignmentExpression
def p_assignmentExpression(p):
    'assignmentExpression : variableDeclaration SET factor'


# relationExpression
def p_relationExpression(p):
    'relationExpression : sumExpression relationExpressionPrime'


# relationExpressionPrime
def p_relationExpressionPrime_relation(p):
    'relationExpressionPrime : relationOperator sumExpression relationExpressionPrime'

def p_relationExpressionPrime_empty(p):
    'relationExpressionPrime : '
    p[0] = None


# relationOperator
def p_relationOperator_equal(p):
    'relationOperator : EQUAL'

def p_relationOperator_less_equal(p):
    'relationOperator : LESS_EQUAL'

def p_relationOperator_greater_equal(p):
    'relationOperator : GREATER_EQUAL'

def p_relationOperator_not_equal(p):
    'relationOperator : NOT_EQUAL'

def p_relationOperator_less(p):
    'relationOperator : LESS'

def p_relationOperator_greater(p):
    'relationOperator : GREATER'


# sumExpression
# TODO