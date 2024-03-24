from typing import List, Tuple


from ..my_code import rolling_max
import unittest

class TestRollingMax(unittest.TestCase):

    def test_rolling_max(self):
        input_data = [(1, 2, 3, 4, 5), (10, 9, 8, 7, 6), (100, 200, 150, 300, 250), (5, 5, 5, 5, 5), (0, 0, 0, 0, 0)]
        expected_output = [[1, 2, 3, 4, 5], [10, 10, 10, 10, 10], [100, 200, 200, 300, 300], [5, 5, 5, 5, 5], [0, 0, 0, 0, 0]]

        for i in range(len(input_data)):
            self.assertEqual(rolling_max(list(input_data[i])), expected_output[i])

if __name__ == '__main__':
    unittest.main()