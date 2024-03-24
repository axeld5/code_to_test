from typing import List, Tuple


from ..my_code import intersperse
import unittest

class TestIntersperse(unittest.TestCase):

    def test_intersperse(self):
        self.assertEqual(intersperse([1, 2, 3, 4], 0), [1, 0, 2, 0, 3, 0, 4])
        self.assertEqual(intersperse([5, 10, 15, 20], -1), [5, -1, 10, -1, 15, -1, 20])
        self.assertEqual(intersperse([100, 200, 300], 999), [100, 999, 200, 999, 300])
        self.assertEqual(intersperse([], 5), [])
        self.assertEqual(intersperse([7, 8, 9], 100), [7, 100, 8, 100, 9])

if __name__ == '__main__':
    unittest.main()