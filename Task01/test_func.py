import unittest
from triangle_func import IncorrectTriangleSides, get_triangle_type


class TestGetTriangleTypeFunction(unittest.TestCase):

    def test_isosceles_triangle(self):
        self.assertEqual(get_triangle_type(7, 7, 10), 'isosceles')

    def test_equilateral_triangle(self):
        self.assertEqual(get_triangle_type(7, 7, 7), 'equilateral')

    def test_nonequilateral_triangle(self):
        self.assertEqual(get_triangle_type(7, 9, 11), 'nonequilateral')

    def test_type_error(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type('1', '7', '1')

    def test_incorrect_sides(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(7, 5, 1)


if __name__ == '__main__':
    unittest.main()