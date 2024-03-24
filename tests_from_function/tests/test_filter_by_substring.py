from typing import List, Tuple


from ..my_code import filter_by_substring
import unittest

class TestFilterBySubstring(unittest.TestCase):

    def test_filter_by_substring(self):
        self.assertEqual(filter_by_substring(["apple", "banana", "cherry"], "an"), ['banana'])
        self.assertEqual(filter_by_substring(["hello", "world", "python"], "o"), ['hello', 'world', 'python'])
        self.assertEqual(filter_by_substring(["cat", "dog", "fish"], "g"), ['dog'])
        self.assertEqual(filter_by_substring(["sun", "moon", "stars"], "s"), ['sun', 'stars'])
        self.assertEqual(filter_by_substring(["car", "bike", "bus"], "k"), ['bike'])

if __name__ == '__main__':
    unittest.main()