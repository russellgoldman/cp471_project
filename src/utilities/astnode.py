# https://ply.readthedocs.io/en/latest/ply.html#ast-construction
# node for a non-terminal (variable) instance in an Abstract Syntax Tree
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'syntax')))
from typing import List, Tuple
import enum

class SymbolType(enum.Enum):
    NONTERMINAL = 'nonterminal'
    TERMINAL = 'terminal'

class NonTerminal(enum.Enum):
    PROGRAM = 'program'
    NEXT_LINE = 'nextLine'
    NEXT_LINE_PRIME = 'nextLinePrime'
    STATEMENT = 'statement'
    EXPRESSION = 'expression'
    ASSIGNMENT_EXPRESSION = 'assignmentExpression'
    VARIABLE_DECLARATION = 'variableDeclaration'
    FACTOR = 'factor'

def create_ast_node(type: NonTerminal, children: List[Tuple[str, SymbolType]] = None):
    return ASTNode(type, children)

class ASTNode:
    def __init__(self, type, children):
        self.type = type
        self.children = children