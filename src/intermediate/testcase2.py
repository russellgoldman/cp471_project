import unittest
import sys, os
from codegen import CodeGen
sys.path.append(os.path.abspath(os.path.join('..', 'semantic')))
from ez_parser import Parser

class TestCase2(unittest.TestCase):
    def test_bedmas_operations(self) -> None:
        source_f = open('./given/testcase2.ez', 'r')
        source = source_f.read()
        source_f.close()

        expected_f = open('./expected_codegen/testcase2.txt', 'r')
        expected = expected_f.read()
        expected_f.close()

        # build parser
        p = Parser()
        p.build()
        # generate parse tree
        given_tree = p.parse(source)
        c = CodeGen()
        c.build(given_tree)
        given_code = c.generate()
        self.assertEqual(str(given_code), expected)


if __name__ == '__main__':
    unittest.main()