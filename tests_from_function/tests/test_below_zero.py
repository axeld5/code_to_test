from typing import List, Tuple


from ..my_code import below_zero
import unittest

class TestBelowZero(unittest.TestCase):

    def test_below_zero(self):
        self.assertEqual(below_zero([1, 2, 3, 4, 5]), False)
        self.assertEqual(below_zero([-1, -2, -3, -4, -5]), True)
        self.assertEqual(below_zero([10, -5, 3, -2, 1]), False)
        self.assertEqual(below_zero([100, 200, -300, 400, -500]), True)
        self.assertEqual(below_zero([0, 0, 0, 0, 0]), False)