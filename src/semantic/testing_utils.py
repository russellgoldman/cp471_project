import sys, os
import unittest
sys.path.append(os.path.abspath(os.path.join('..', 'syntax')))
from ez_parser import Parser
sys.path.append(os.path.abspath(os.path.join('..', 'utilities')))
from syntax_tree import TreeNode, convert_parse_to_abstract, compare_trees

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