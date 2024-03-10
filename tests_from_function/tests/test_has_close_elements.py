import unittest
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                distance = abs(elem - elem2)
                if distance < threshold:
                    return True

    return False

class TestHasCloseElements(unittest.TestCase):

    def test_has_close_elements(self):
        test_cases = [([1.0, 2.0, 3.0], 0.5, False),
                      ([10.5, 15.2, 20.7], 5.0, True),
                      ([0.1, 0.2, 0.3], 0.01, False),
                      ([100.0, 200.0, 300.0], 50.0, False),
                      ([-5.0, -3.0, 0.0, 2.0], 2.5, True)]

        for numbers, threshold, expected_output in test_cases:
            with self.subTest(numbers=numbers, threshold=threshold, expected_output=expected_output):
                self.assertEqual(has_close_elements(numbers, threshold), expected_output)

if __name__ == '__main__':
    unittest.main()