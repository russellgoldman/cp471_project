import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'utilities')))

import unittest
from ez_parser import Parser
from syntax_tree import TreeNode, get_qtree_representation

def assert_syntax(self, source, expected_syntax, debug=False):
    # build parser
    p = Parser()
    p.build()
    # generate parse tree
    given_tree = p.parse(source, debug)
    # check that the syntax is correct
    compare_trees(self, given_tree, expected_syntax)

def compare_trees(self, given_tree: TreeNode, expected_syntax: str):
    given_syntax = get_qtree_representation(given_tree)
    self.assertEqual(given_syntax, expected_syntax)