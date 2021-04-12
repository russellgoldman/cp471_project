import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'utilities')))

import unittest
from ez_parser import Parser
from syntax_tree import TreeNode, get_qtree_representation, convert_parse_to_abstract

def assert_syntax(self, source, expected_syntax, debug=False):
    # build parser
    p = Parser()
    p.build()
    # generate parse tree
    given_tree = p.parse(source, debug)
    # check that the syntax is correct
    compare_trees(self, given_tree, expected_syntax)

def assert_ast(self, source, expected_abstract, debug=False):
    # build parser
    p = Parser()
    p.build()
    # generate parse tree
    given_tree = p.parse(source, debug)
    # convert to abstract
    given_ast = convert_parse_to_abstract(given_tree)
    # check that the ast is correct
    compare_trees(self, given_ast, expected_abstract)

def compare_trees(self, given_tree: TreeNode, expected_qtree: str):
    given_qtree = get_qtree_representation(given_tree)
    self.assertEqual(given_qtree, expected_qtree)