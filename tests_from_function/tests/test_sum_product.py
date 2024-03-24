import unittest
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    sum_value = 0
    prod_value = 1

    for n in numbers:
        sum_value += n
        prod_value *= n
    return sum_value, prod_value

class TestSumProduct(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sum_product([]), (0, 1))

    def test_positive_numbers(self):
        self.assertEqual(sum_product([1, 2, 3]), (6, 6))

    def test_large_numbers(self):
        self.assertEqual(sum_product([10, 20, 30, 40]), (100, 240000))

    def test_mixed_numbers(self):
        self.assertEqual(sum_product([-5, 5, -10]), (-10, 250))

    def test_zero_in_list(self):
        self.assertEqual(sum_product([100, 0, 50]), (150, 0))

if __name__ == '__main__':
    unittest.main()