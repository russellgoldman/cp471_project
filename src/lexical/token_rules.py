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
number_count = 0
string_count = 0
boolean_count = 0
function_count = 0
object_count = 0
prepare_new_scope = False
new_scope = False
prev_tok = None

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
    global for_count, while_count
    global number_count, string_count, boolean_count, function_count
    global prepare_new_scope, new_scope, prev_tok

    # If
    if t.value == 'if':
        if_count += 1
        current_scope = 'if_{}'.format(if_count)
        new_scope = True
    # Elif
    elif t.value == 'elif':
        elif_count += 1
        current_scope = 'elif_{}'.format(elif_count)
        new_scope = True
    # Else
    elif t.value == 'else':
        else_count += 1
        current_scope = 'else_{}'.format(else_count)
        new_scope = True
    # For
    elif t.value == 'for':
        for_count += 1
        current_scope = 'for_{}'.format(for_count)
        new_scope = True
    # While
    elif t.value == 'while':
        while_count += 1
        current_scope = 'while_{}'.format(while_count)
        new_scope = True
    # Number
    elif t.value == 'Number':
        prev_tok = t.value
    # String
    elif t.value == 'String':
        prev_tok = t.value
    # Boolean
    elif t.value == 'Boolean':
        prev_tok = t.value
    # Function
    elif t.value == 'Function':
        function_count += 1
        prev_tok = t.value
    elif prev_tok == 'Function':
        current_scope = 'function_{}'.format(function_count)
        prepare_new_scope = True
    # Object
    elif t.value == 'Object':
        object_count += 1
        prev_tok = t.value
    elif prev_tok == 'Object':
        current_scope = 'object_{}'.format(object_count)

    if new_scope:
        current_node = symbol_table.create_node(current_scope, current_node)
        new_scope = False
    if prepare_new_scope:
        prepare_new_scope = False
        new_scope = True
    
    t.type = reserved.get(t.value, 'ID')
    if t.type == 'ID':
        # add ID to current scope of symbol table
        if prev_tok != None:
            current_node.add_record(t.value, prev_tok)
        prev_tok = None

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
