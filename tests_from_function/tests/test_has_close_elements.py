from typing import List, Tuple


from ..my_code import has_close_elements
import unittest

class TestHasCloseElements(unittest.TestCase):

    def test_has_close_elements_false_1(self):
        self.assertEqual(has_close_elements([1.0, 2.0, 3.0, 4.0], 0.5), False)

    def test_has_close_elements_false_2(self):
        self.assertEqual(has_close_elements([10.5, 20.3, 30.7], 5.0), False)

    def test_has_close_elements_false_3(self):
        self.assertEqual(has_close_elements([-5.0, -3.0, 0.0, 2.0], 1.0), False)

    def test_has_close_elements_false_4(self):
        self.assertEqual(has_close_elements([100.0, 105.0, 110.0], 2.0), False)

    def test_has_close_elements_false_5(self):
        self.assertEqual(has_close_elements([2.5, 5.0, 7.5, 10.0], 1.0), False)