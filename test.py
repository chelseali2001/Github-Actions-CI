import unittest
import example


class SimpleTest(unittest.TestCase):
    def test_calculator(self):
        self.assertEqual(example.add(4, 2), 6)

    def test_calculator0(self):
        self.assertEqual(example.sub(4, 2), 2)

    def test_calculator1(self):
        self.assertEqual(example.mul(4, 2), 8)

    def test_calculator2(self):
        self.assertEqual(example.div(4, 2), 2)


if __name__ == '__main__':
    unittest.main()
