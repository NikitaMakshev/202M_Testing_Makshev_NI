import pytest
from triangle_class import Triangle
from triangle_func import IncorrectTriangleSides


class TestTriangleClass:
    def test_triangle_create(self):
        triangle = Triangle(7, 7, 10)
        assert triangle.a == 7
        assert triangle.b == 7
        assert triangle.c == 10

    def test_triangle_create_with_incorrect_type(self):
        with pytest.raises(IncorrectTriangleSides):
            Triangle('1','7','1')

    def test_triangle_create_with_incorrect_sides(self):
        with pytest.raises(IncorrectTriangleSides):
            Triangle(7, 5, 1)

    def test_triangle_type_nonequilateral(self):
        assert Triangle(7, 9, 11).triangle_type() == 'nonequilateral'

    def test_triangle_type_equilateral(self):
        assert Triangle(7, 7, 7).triangle_type() == 'equilateral'

    def test_triangle_type_isosceles(self):
        assert Triangle(7, 7, 10).triangle_type() == 'isosceles'

    def test_triangle_perimeter(self):
        assert Triangle(7, 7, 10).perimeter() == 24