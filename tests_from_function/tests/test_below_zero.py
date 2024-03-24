import unittest

from typing import List, Tuple

def below_zero(operations: List[int]) -> bool:
    balance = 0

    for op in operations:
        balance += op
        if balance < 0:
            return True

    return False

class TestBelowZero(unittest.TestCase):

    def test_below_zero_false(self):
        self.assertEqual(below_zero([1, 2, 3, -6, 5]), False)
        self.assertEqual(below_zero([10, -5, 3, 2, -8]), False)
        self.assertEqual(below_zero([0, 0, 0, 0, 0]), False)

    def test_below_zero_true(self):
        self.assertEqual(below_zero([-1, -2, -3, -4, -5]), True)
        self.assertEqual(below_zero([100, 50, -200, 150, 75]), True)

if __name__ == '__main__':
    unittest.main()