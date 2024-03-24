from typing import List, Tuple


from ..my_code import mean_absolute_deviation
import unittest

class TestMeanAbsoluteDeviation(unittest.TestCase):

    def test_mean_absolute_deviation(self):
        self.assertAlmostEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 5.0]), 1.2)
        self.assertAlmostEqual(mean_absolute_deviation([10.5, 20.7, 15.3, 18.9]), 3.45)
        self.assertAlmostEqual(mean_absolute_deviation([-5.0, -2.0, 0.0, 3.0, 5.0]), 3.04)
        self.assertAlmostEqual(mean_absolute_deviation([100.0, 200.0, 150.0, 120.0]), 32.5)
        self.assertAlmostEqual(mean_absolute_deviation([3.14, 2.71, 1.618, 0.577]), 0.91375)

if __name__ == '__main__':
    unittest.main()