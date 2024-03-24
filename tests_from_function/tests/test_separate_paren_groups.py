from typing import List, Tuple


from ..my_code import separate_paren_groups
import unittest

class TestSeparateParenGroups(unittest.TestCase):

    def test_separate_paren_groups(self):
        input_list = ["(a)", "(a(b))", "(a(b(c)))", "(a(b(c)))(d)", "(a(b(c)))(d(e))"]
        output_list = [['()'], ['(())'], ['((()))'], ['((()))', '()'], ['((()))', '(())']]

        for i in range(len(input_list)):
            self.assertEqual(separate_paren_groups(input_list[i]), output_list[i])

if __name__ == '__main__':
    unittest.main()