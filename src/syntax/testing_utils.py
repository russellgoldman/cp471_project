import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'utilities')))

import unittest
from ez_parser import Parser
from syntax_tree import TreeNode, compare_trees

def assert_syntax(self, source, expected_syntax, debug=False):
    # build parser
    p = Parser()
    p.build()
    # generate parse tree
    given_tree = p.parse(source, debug)
    # check that the syntax is correct
    compare_trees(self, given_tree, expected_syntax)