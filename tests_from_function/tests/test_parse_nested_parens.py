from typing import List, Tuple


from ..my_code import parse_nested_parens
import unittest

class TestParseNestedParens(unittest.TestCase):

    def test_example_cases(self):
        input_list = ["(()) ()", "((()))", "((()()()))", "()", "(()) (()())"]
        output_list = [[2, 1], [3], [3], [1], [2, 2]]
        for i in range(len(input_list)):
            self.assertEqual(parse_nested_parens(input_list[i]), output_list[i])

if __name__ == '__main__':
    unittest.main()