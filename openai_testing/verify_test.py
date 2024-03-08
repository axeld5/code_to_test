from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                distance = abs(elem - elem2)
                if distance < threshold:
                    return True

    return False

import unittest

class TestHasCloseElements(unittest.TestCase):

    def test_has_close_elements_false(self):
        self.assertEqual(has_close_elements([1.0, 2.0, 3.0], 0.5), False)
        self.assertEqual(has_close_elements([0.1, 0.2, 0.3, 0.4], 0.05), False)
        self.assertEqual(has_close_elements([100.0, 105.0, 110.0], 1.0), False)

    def test_has_close_elements_true(self):
        self.assertEqual(has_close_elements([10.5, 15.2, 20.7], 5.0), True)
        self.assertEqual(has_close_elements([-5.0, -3.0, 0.0, 2.0], 2.5), True)

if __name__ == '__main__':
    unittest.main()