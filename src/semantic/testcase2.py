import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'utilities')))

from ez_parser import Parser

class TestCase2(unittest.TestCase):
    def test_bedmas_operations(self) -> None:
        source_f = open('./given/testcase2.ez', 'r')
        source = source_f.read()
        source_f.close()

        expected_f = open('./expected/testcase2.txt', 'r')
        expected = expected_f.read()
        expected_f.close()

        # build parser
        p = Parser()
        p.build()
        # generate parse tree
        given_tree = p.parse(source)
        self.assertEqual(str(given_tree), expected)


if __name__ == '__main__':
    unittest.main()