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
    # Look up symbol type in symbol table
    # t.value = (t.value, symbol_lookup(t.value))
    # Check if ID is a reserved word
    t.type = reserved.get(t.value, 'ID')
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
