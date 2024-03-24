import unittest
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

class TestFilterBySubstring(unittest.TestCase):

    def test_example_1(self):
        input_strings = ["apple", "banana", "cherry"]
        input_substring = "an"
        expected_output = ["banana"]
        self.assertEqual(filter_by_substring(input_strings, input_substring), expected_output)

    def test_example_2(self):
        input_strings = ["hello", "world", "python"]
        input_substring = "o"
        expected_output = ["hello", "world", "python"]
        self.assertEqual(filter_by_substring(input_strings, input_substring), expected_output)

    def test_example_3(self):
        input_strings = ["cat", "dog", "rabbit"]
        input_substring = "at"
        expected_output = ["cat"]
        self.assertEqual(filter_by_substring(input_strings, input_substring), expected_output)

    def test_example_4(self):
        input_strings = ["sun", "moon", "stars"]
        input_substring = "moon"
        expected_output = ["moon"]
        self.assertEqual(filter_by_substring(input_strings, input_substring), expected_output)

    def test_example_5(self):
        input_strings = ["car", "bike", "bus"]
        input_substring = "truck"
        expected_output = []
        self.assertEqual(filter_by_substring(input_strings, input_substring), expected_output)

if __name__ == '__main__':
    unittest.main()