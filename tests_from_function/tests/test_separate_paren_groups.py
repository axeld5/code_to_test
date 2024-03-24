import unittest
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    result = []
    current_string = []
    current_depth = 0

    for c in paren_string:
        if c == '(':
            current_depth += 1
            current_string.append(c)
        elif c == ')':
            current_depth -= 1
            current_string.append(c)

            if current_depth == 0:
                result.append(''.join(current_string))
                current_string.clear()

    return result


class TestSeparateParenGroups(unittest.TestCase):

    def test_separate_paren_groups(self):
        input_list = ["(a(b)c)", "(a(b(c)d)e)", "(a(b(c)d)e(f(g)))", "()", "(a)"]
        output_list = [['(())'], ['((()))'], ['((())(()))'], ['()'], ['()']]

        for i in range(len(input_list)):
            self.assertEqual(separate_paren_groups(input_list[i]), output_list[i])


if __name__ == '__main__':
    unittest.main()