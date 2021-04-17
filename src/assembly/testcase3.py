import unittest
import sys, os
from assemblygen import AssemblyGen

class TestCase1(unittest.TestCase):
    def test_for_loop(self) -> None:
        source_f = open('./given/testcase3.txt', 'r')
        source = source_f.read()
        source_f.close()

        expected_f = open('./expected_assembly/testcase3.txt', 'r')
        expected = expected_f.read()
        expected_f.close()

        a = AssemblyGen()
        given_assembly = a.generate(source)
        self.assertEqual(str(given_assembly), expected)
if __name__ == '__main__':
    unittest.main()