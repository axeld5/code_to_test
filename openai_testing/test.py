import unittest

def add(a:float, b:float) -> float:
    return a+b

class TestAddFunction(unittest.TestCase):

    def test_add(self):
        self.assertAlmostEqual(add(1.5, 2.5), 4.0)
        self.assertAlmostEqual(add(-1.0, 1.0), 0.0)
        self.assertAlmostEqual(add(0.0, 0.0), 0.0)
        self.assertAlmostEqual(add(-1.5, -2.5), -4.0)

if __name__ == '__main__':
    unittest.main()