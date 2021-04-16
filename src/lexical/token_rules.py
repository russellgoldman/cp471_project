import sys, os, pdb
sys.path.append(os.path.abspath(os.path.join('..')))
from utilities.symbol_table_v2 import symbol_table

current_scope = 'global'
current_node = symbol_table.get_node_by_scope(current_scope)
print(current_node)

if_count = 0
elif_count = 0
else_count = 0
for_count = 0
while_count = 0
function_count = 0

prev = ''

# --------------------
# Reserved Keywords
# --------------------
reserved = {
    'if': 'IF',
    'elif': 'ELIF',
    'else': 'ELSE',
    'for': 'FOR',
    'while': 'WHILE',
    'this': 'THIS',
    'return': 'RETURN',
    'Import': 'IMPORT',
    'Number': 'NUMBER',
    'String': 'STRING',
    'Boolean': 'BOOLEAN',
    'Function': 'FUNCTION',
    'Object': 'OBJECT',
    'print': 'PRINT',
    'out': 'OUT',
    'input': 'INPUT',
    'in': 'IN',
    'True': 'TRUE',
    'False': 'FALSE',
}

# --------------------
# Structural Keywords
# --------------------
structural = {
    '(': 'LPAREN',
    ')': 'RPAREN',
    '[': 'LSQUARE',
    ']': 'RSQUARE',
    '{': 'LCURLY',
    '}': 'RCURLY',
    ';': 'SEMICOLON',
    '+': 'PLUS',
    '-': 'MINUS',
    '*': 'MULTIPLY',
    '/': 'DIVIDE',
    '%': 'MODULUS',
    '++': 'INCREMENT',
    '--': 'DECREMENT',
    '==': 'EQUAL',
    '<': 'LESS',
    '>': 'GREATER',
    '<=': 'LESS_EQUAL',
    '>=': 'GREATER_EQUAL',
    '!=': 'NOT_EQUAL',
    '->': 'RETURNS',
    '=': 'SET',
    '<<': 'OUT_PIPE',
    '>>': 'IN_PIPE'
}


# --------------------
# Token Names
# --------------------
tokens = [
    'ID',
    'OPERATOR',
    'NUMBER_LITERAL',
    'STRING_LITERAL',
    'SEPARATOR',
]   + list(reserved.values())       \
    + list(structural.values())

# --------------------
# Token Definitions
# --------------------
# Tokens can be defined as strings or as functions using regex
def t_COMMENT(t):
    r'@![\ -~]*|@!![\ -~]*!!@'
    pass

def t_ID(t):
    r'([A-Za-z]|_)([A-Za-z]|[0-9]|_)*'
    # Check if ID is a reserved word
    global current_scope, current_node
    global if_count, elif_count, else_count
    global for_count, while_count, function_count, prev
    changes = True

    # If
    if t.value == 'if':
        if_count += 1
        current_scope = 'if_{}'.format(if_count)
    # Elif
    elif t.value == 'elif':
        elif_count += 1
        current_scope = 'elif_{}'.format(elif_count)
    # Else
    elif t.value == 'else':
        else_count += 1
        current_scope = 'else_{}'.format(else_count)
    # For
    elif t.value == 'for':
        for_count += 1
        current_scope = 'for_{}'.format(for_count)
    # While
    elif t.value == 'while':
        while_count += 1
        current_scope = 'while_{}'.format(while_count)
    # Function
    elif t.value == 'Function':
        function_count += 1
        prev = t
    elif prev == 'Function':
        current_scope = 'function_{}'.format(function_count)
        return t
    else:
        changes = False

    if changes:
        current_node = symbol_table.create_node(current_scope, current_node)
    
    t.type = reserved.get(t.value, 'ID')
    if t.type == 'ID':
        # add ID to current scope of symbol table
        current_node.add_record(t.value)

    return t


def t_SEPARATOR(t):
    r'\(|\)|{|}|\[|\]|;|,|\#|@|->|\|.'

    t.type = structural.get(t.value, 'SEPARATOR')
    return t


def t_OPERATOR(t):
    r'==|<=|>=|!=|>>|<<|\*\*|\+\+|--|>|<|=|\+|-|\*|/|%'
    t.type = structural.get(t.value, 'OPERATOR')
    return t


def t_NUMBER_LITERAL(t):
    r'[0-9]+|([0-9]+.[0-9]+)'
    t.value = int(t.value)
    return t


def t_STRING_LITERAL(t):
    r'(\"[\ -~]*\")|(\'[\ -~]*\')'
    return t


# Ignore spaces and tabs
t_ignore = ' \t\n'

# Error handling rule


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
