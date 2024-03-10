import unittest
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    def parse_paren_group(s):
        depth = 0
        max_depth = 0
        for c in s:
            if c == '(':
                depth += 1
                max_depth = max(depth, max_depth)
            else:
                depth -= 1

        return max_depth

    return [parse_paren_group(x) for x in paren_string.split(' ') if x]

class TestParseNestedParens(unittest.TestCase):

    def test_parse_nested_parens(self):
        input_list = ["(()) ()", "((()))", "((()()()))", "()", "(()) (()())"]
        output_list = [[2, 1], [3], [3], [1], [2, 2]]

        for i in range(len(input_list)):
            self.assertEqual(parse_nested_parens(input_list[i]), output_list[i])

if __name__ == '__main__':
    unittest.main()