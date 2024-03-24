import unittest
from typing import List, Tuple
def rolling_max(numbers: List[int]) -> List[int]:
    running_max = None
    result = []

    for n in numbers:
        if running_max is None:
            running_max = n
        else:
            running_max = max(running_max, n)

        result.append(running_max)

    return result

class TestRollingMax(unittest.TestCase):

    def test_rolling_max(self):
        input_data = [(1, 2, 3, 4, 5), (10, 9, 8, 7, 6), (100, 200, 150, 300, 250), (5, 4, 3, 2, 1), (-1, -2, -3, -4, -5)]
        expected_output = [[1, 2, 3, 4, 5], [10, 10, 10, 10, 10], [100, 200, 200, 300, 300], [5, 5, 5, 5, 5], [-1, -1, -1, -1, -1]]

        for i in range(len(input_data)):
            with self.subTest(input_data=input_data[i], expected_output=expected_output[i]):
                self.assertEqual(rolling_max(list(input_data[i])), expected_output[i])

if __name__ == '__main__':
    unittest.main()