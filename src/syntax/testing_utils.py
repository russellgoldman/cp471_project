import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'utilities')))

import unittest
from ez_parser import Parser
from astnode import ASTNode, SymbolType

def assert_syntax(self, source, expected_syntax, debug=False):
    p = Parser()
    p.build()
    given_tree = p.parse(source, debug)

    # check that the syntax is correct
    compare_ast_trees(self, given_tree, expected_syntax)
    # self.assertEqual(str(given_syntax), expected_syntax)

def compare_ast_trees(self, given_tree: ASTNode, expected_syntax: str):
    # test
    given_syntax = get_qtree_representation(given_tree)
    self.assertEqual(given_syntax, expected_syntax)

def get_qtree_representation(node: ASTNode):
    tree_str = get_qtree_rep_aux(node, 1)
    return '\Tree {}'.format(tree_str)

# https://www.ling.upenn.edu/advice/latex/qtree/qtreenotes.pdf
def get_qtree_rep_aux(node: ASTNode, level):
    VALUE       = 0
    SYMBOL_TYPE = 1

    if node.children == None:
        return '[.{} ]'.format(node.type.value)
    elif len(node.children) == 1:
        child = node.children[0]

        if child[SYMBOL_TYPE] == SymbolType.TERMINAL:
            child_str = '[.{} ]'.format(child[VALUE])
        else:
            child_str = get_qtree_rep_aux(child[VALUE], level)

        return '[.{} {} ]'.format(node.type.value, child_str)
    else:
        child_str = '[.{}\n'.format(node.type.value)

        for child in node.children:
            child_str += '\t' * level
            if child[SYMBOL_TYPE] == SymbolType.TERMINAL:
                child_str += '[.{} ]\n'.format(child[VALUE])
            else:
                child_str += get_qtree_rep_aux(child[VALUE], level + 1)
                child_str += '\n'

        child_str += '\t' * (level - 1)
        child_str += ']'
        return child_str