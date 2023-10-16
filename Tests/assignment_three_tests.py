import unittest
import assignment_three


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(52, assignment_three.calculateSurfaceArea(3, 4, 2))


if __name__ == '__main__':
    unittest.main()
