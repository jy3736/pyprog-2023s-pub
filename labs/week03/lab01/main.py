import unittest
from lab01 import merge_numbers

class TestMergeNumbers(unittest.TestCase):
    def test_case_1(self):
        result = merge_numbers(12, 34)
        self.assertEqual(result, 1234)
    
    def test_case_2(self):
        result = merge_numbers(11, 22)
        self.assertEqual(result, 1122)
    
    def test_case_3(self):
        result = merge_numbers(13, 24)
        self.assertEqual(result, 1324)

if __name__ == '__main__':
    unittest.main()