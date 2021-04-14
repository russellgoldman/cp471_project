# https://ply.readthedocs.io/en/latest/ply.html#ast-construction
# node for a non-terminal (variable) instance in an Abstract Syntax Tree
import enum
from typing import List, Tuple
import sys
import os
sys.path.append(os.path.abspath(os.path.join('..', 'syntax')))


class SymbolType(enum.Enum):
    NONTERMINAL = 'nonterminal'
    TERMINAL = 'terminal'


class NonTerminal(enum.Enum):
    PROGRAM = 'program'
    NEXT_LINE = 'nextLine'
    NEXT_LINE_PRIME = 'nextLinePrime'
    STATEMENT = 'statement'
    IF_STATEMENT = 'ifStatement'
    ITERATION_STATEMENT = 'iterationStatement'
    ITERATION_OPERATOR = 'iterationOperator'
    STATEMENT_BODY = 'statementBody'
    STATEMENT_BODY_EXPRESSION = 'statementBodyExpression'
    ELIF_ELSE_STATEMENT = 'elifElseStatement'
    EXPRESSION = 'expression'
    ASSIGNMENT_EXPRESSION = 'assignmentExpression'
    ITERATION_EXPRESSION = 'iterationExpression'
    SUM_EXPRESSION = 'sumExpression'
    SUM_EXPRESSION_PRIME = 'sumExpressionPrime'
    MULTIPLY_EXPRESSION = 'multiplyExpression'
    MULTIPLY_EXPRESSION_PRIME = 'multiplyExpressionPrime'
    RELATION_EXPRESSION = 'relationExpression'
    RELATION_EXPRESSION_PRIME = 'relationExpressionPrime'
    RELATION_OPERATOR = 'relationOperator'
    VARIABLE_DECLARATION = 'variableDeclaration'
    SUM_OPERATOR = 'sumOperator'
    MULTIPLY_OPERATOR = 'multiplyOperator'
    FACTOR = 'factor'
    MUTABLE = 'mutable'
    IMMUTABLE = 'immutable'
    CONSTANT = 'constant'
    INPUT_STATEMENT = 'inputStatement'
    IN_STREAM = 'inStream'
    OUTPUT_STATEMENT = 'outputStatement'
    OUT_FUNCTION = 'outFunction'


class TreeNode:
    def __init__(self, type, children):
        self.type = type
        self.children = children


class Terminal:
    def __init__(self, value):
        self.value = value


def terminal_value(node: TreeNode):
    # When converting to AST we sometimes need a terminal to have
    # a .value attribute
    return Terminal(node)


def create_tree_node(type: NonTerminal, children: List[Tuple[str, SymbolType]] = None):
    return TreeNode(type, children)


def get_qtree_representation(node: TreeNode):
    tree_str = _get_qtree_rep_aux(node, 1)
    return '\Tree {}'.format(tree_str)

# Documentation for qtree LaTeX standard
# https://www.ling.upenn.edu/advice/latex/qtree/qtreenotes.pdf


def _get_qtree_rep_aux(node: TreeNode, level):
    VALUE = 0
    SYMBOL_TYPE = 1

    if not(hasattr(node, 'children')):
        return '[.{} ]'.format(node)
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
    VALUE = 0
    SYMBOL_TYPE = 1

    if not(hasattr(node, 'children')):
        # Leaf, return
        return node
    else:
        if len(node.children) == 1:  # 1 child
            # Take whatever we retrieve
            newNode = convert_parse_to_abstract(node.children[0][VALUE])
        if len(node.children) == 2:  # 2 children
            if node.children[0][SYMBOL_TYPE] == SymbolType.TERMINAL:
                # If left is a terminal, we likely want the right
                # Take whatever right is - as if it was a single child
                newNode = convert_parse_to_abstract(node.children[1][VALUE])
            else:  # Left is nonterminal
                parent = node.type  # Current node should remain the parent
                children = [(convert_parse_to_abstract(
                    node.children[0][VALUE]), node.children[0][SYMBOL_TYPE])]
                children.append((convert_parse_to_abstract(
                    node.children[1][VALUE]), node.children[1][SYMBOL_TYPE]))
                # Create the node, assigning the 2 children we retrieved
                newNode = create_tree_node(parent, children)
        elif len(node.children) == 3:  # 3 children
            children = [(convert_parse_to_abstract(
                node.children[0][VALUE]), node.children[0][SYMBOL_TYPE])]
            children.append((convert_parse_to_abstract(
                node.children[2][VALUE]), node.children[2][SYMBOL_TYPE]))
            # Middle child is parent
            parent = convert_parse_to_abstract(node.children[1][VALUE])
            parent = terminal_value(parent)
            # Create the node, assigning left and right siblings as children
            newNode = create_tree_node(parent, children)
        return newNode

def compare_trees(self, given_tree: TreeNode, expected_qtree: str):
    given_qtree = get_qtree_representation(given_tree)
    self.assertEqual(given_qtree, expected_qtree)
