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

class TreeNode:
    def __init__(self, type, children):
        self.type = type
        self.children = children

def create_tree_node(type: NonTerminal, children: List[Tuple[str, SymbolType]] = None):
    return TreeNode(type, children)

def get_qtree_representation(node: TreeNode):
    tree_str = _get_qtree_rep_aux(node, 1)
    return '\Tree {}'.format(tree_str)

# Documentation for qtree LaTeX standard
# https://www.ling.upenn.edu/advice/latex/qtree/qtreenotes.pdf
def _get_qtree_rep_aux(node: TreeNode, level):
    VALUE       = 0
    SYMBOL_TYPE = 1

    if node.children == None:
        return '[.{} ]'.format(node.type.value)
    elif len(node.children) == 1:
        child = node.children[0]

        if child[SYMBOL_TYPE] == SymbolType.TERMINAL:
            child_str = '[.{} ]'.format(child[VALUE])
        else:
            child_str = _get_qtree_rep_aux(child[VALUE], level)

        return '[.{} {} ]'.format(node.type.value, child_str)
    else:
        child_str = '[.{}\n'.format(node.type.value)

        for child in node.children:
            child_str += '\t' * level

            if child[SYMBOL_TYPE] == SymbolType.TERMINAL:
                child_str += '[.{} ]\n'.format(child[VALUE])
            else:
                child_str += _get_qtree_rep_aux(child[VALUE], level + 1)
                child_str += '\n'

        child_str += '\t' * (level - 1)
        child_str += ']'
        return child_str

# Converts a Parse Tree to an Abstract Syntax Tree (AST)
def convert_parse_to_abstract(node: TreeNode):
    # todo
    pass