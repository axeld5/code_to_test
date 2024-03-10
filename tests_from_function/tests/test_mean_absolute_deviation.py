import unittest
from typing import List, Tuple

def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers) / len(numbers)

class TestMeanAbsoluteDeviation(unittest.TestCase):

    def test_mean_absolute_deviation(self):
        input_list = [(1.5, 2.5, 3.5, 4.5), (10.0, 20.0, 30.0, 40.0, 50.0), (0.1, 0.2, 0.3, 0.4, 0.5), (-5.5, -4.5, -3.5, -2.5, -1.5), (100.5, 200.5, 300.5, 400.5)]
        output_list = [1.0, 12.0, 0.12, 1.2, 100.0]

        for i in range(len(input_list)):
            self.assertEqual(mean_absolute_deviation(list(input_list[i])), output_list[i])

if __name__ == '__main__':
    unittest.main()