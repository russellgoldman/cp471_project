import unittest

class TestCase2(unittest.TestCase):
    def test_for_loop(self) -> None:
        source_f = open('./given/testcase3.ez', 'r')
        source = source_f.read()
        source_f.close()

        expected_f = open('./expected/testcase3.txt', 'r')
        expected = expected_f.read()
        expected_f.close()

if __name__ == '__main__':
    unittest.main()