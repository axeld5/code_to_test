from typing import List, Tuple


from ..my_code import truncate_number
import unittest

class TestTruncateNumber(unittest.TestCase):

    def test_truncate_number(self):
        self.assertAlmostEqual(truncate_number(3.14), 0.14000000000000012)
        self.assertAlmostEqual(truncate_number(5.67), 0.6699999999999999)
        self.assertAlmostEqual(truncate_number(10.0), 0.0)
        self.assertAlmostEqual(truncate_number(7.89), 0.8899999999999997)
        self.assertAlmostEqual(truncate_number(-2.5), 0.5)

if __name__ == '__main__':
    unittest.main()