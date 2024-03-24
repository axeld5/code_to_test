import unittest

from typing import List, Tuple

def truncate_number(number: float) -> float:
    return number % 1.0

class TestTruncateNumber(unittest.TestCase):

    def test_truncate_number(self):
        input_list = [5.7, 10.0, 3.14159, -8.9, 0.123]
        output_list = [0.7000000000000002, 0.0, 0.14158999999999988, 0.09999999999999964, 0.123]

        for i in range(len(input_list)):
            self.assertEqual(truncate_number(input_list[i]), output_list[i])

if __name__ == '__main__':
    unittest.main()