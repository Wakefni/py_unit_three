import unittest
import assignment_three



class MyTestCase(unittest.TestCase):

    def test_assignment_three(self):

        self.assertEqual(15, return_addtion.add_two(3, 4, 2))
        self.assertEqual(45, return_addtion.add_two(40, 5))
        # Add two more tests of your own below here

    def test_triangle_area(self):
        self.assertEqual(6.0, triangle_area.area(3, 4, 5))


if __name__ == '__main__':
    unittest.main()
