import unittest
import example

class SimpleTest(unittest.TestCase):
    def test_calculator(self):
        self.assertEqual(example.add(4, 2), 6) 

if __name__ == '__main__':
	unittest.main()
