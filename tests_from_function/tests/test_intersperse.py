import unittest
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    if not numbers:
        return []

    result = []

    for n in numbers[:-1]:
        result.append(n)
        result.append(delimeter)

    result.append(numbers[-1])

    return result

class TestIntersperse(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(intersperse([], 0), [])

    def test_intersperse_with_zero_delimiter(self):
        self.assertEqual(intersperse([1, 2, 3], 0), [1, 0, 2, 0, 3])

    def test_intersperse_with_non_zero_delimiter(self):
        self.assertEqual(intersperse([10, 20, 30, 40], 5), [10, 5, 20, 5, 30, 5, 40])

    def test_intersperse_with_negative_numbers(self):
        self.assertEqual(intersperse([-1, -2, -3, -4], -5), [-1, -5, -2, -5, -3, -5, -4])

    def test_intersperse_with_large_numbers(self):
        self.assertEqual(intersperse([100, 200, 300], 100), [100, 100, 200, 100, 300])

if __name__ == '__main__':
    unittest.main()