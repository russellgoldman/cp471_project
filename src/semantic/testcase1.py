import unittest

class TestCase1(unittest.TestCase):
    def test_while_loop(self) -> None:
        source_f = open('./given/testcase1.ez', 'r')
        source = source_f.read()
        source_f.close()

        expected_f = open('./expected/testcase1.txt', 'r')
        expected = expected_f.read()
        expected_f.close()

if __name__ == '__main__':
    unittest.main()