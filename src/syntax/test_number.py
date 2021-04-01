import unittest
from testing_utils import assert_syntax

# Testing correct syntax parsing of Number token
class TestNumberToken(unittest.TestCase):
    def test_number_declaration(self) -> None:
        source = "Number num = 10;"
        expected_syntax = "Numbernum=10;"
        
        assert_syntax(self, source, expected_syntax)

if __name__ == '__main__':
    unittest.main()