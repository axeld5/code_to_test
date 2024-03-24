from typing import List, Tuple


from ..my_code import sum_product
import unittest

class TestSumProduct(unittest.TestCase):

    def test_sum_product(self):
        self.assertEqual(sum_product([1, 2, 3, 4]), (10, 24))
        self.assertEqual(sum_product([10, 20, 30]), (60, 6000))
        self.assertEqual(sum_product([5, 5, 5, 5, 5]), (25, 3125))
        self.assertEqual(sum_product([0, 1, 2, 3, 4, 5]), (15, 0))
        self.assertEqual(sum_product([-1, -2, -3, -4, -5]), (-15, -120))