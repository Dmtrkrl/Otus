import pytest
from hw2.src.Triangle import *
from hw2.src.Square import *
from hw2.src.Rectangle import *
from hw2.src.Circle import *

@pytest.mark.parametrize('side_a, side_b, side_c, perimeter, area',
                         [
                             (3, 4, 5, 12, 6),
                             (6, 8, 10, 24, 24),
                         ])
def test_triangle(side_a, side_b, side_c, perimeter, area):
    t = Triangle(side_a, side_b, side_c)
    assert t.name == 'Triangle'
    assert t.get_area() == area
    assert t.get_perimeter() == perimeter


@pytest.mark.parametrize('side_a, side_b, side_c',
                         [
                             (-1, 2, -10),
                             (3, 3, 20),
                         ])
def test_triangle_negative(side_a, side_b, side_c):
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)


def test_figure_add_area():
    triangle = Triangle(3, 4, 5)
    square = Square(5)
    rectangle = Rectangle(4, 5)
    circle = Circle(3)
    assert triangle.add_area(square) == 31
    assert triangle.add_area(rectangle) == 26
    assert triangle.add_area(circle) == 34.27433388230814


@pytest.mark.parametrize('side_a, side_b, side_c, expected',
                         [
                             (3, 3, 4, True),
                             (5, 6, 5, True),
                             (7, 8, 9, False),
                         ])
def test_is_isosceles(side_a, side_b, side_c, expected):
    triangle = Triangle(side_a, side_b, side_c)
    assert triangle.is_isosceles() == expected


@pytest.mark.parametrize('side_a, side_b, side_c, expected',
                         [
                             (3, 4, 5, True),
                             (5, 12, 13, True),
                             (6, 8, 7, False),
                         ])
def test_is_right_angled(side_a, side_b, side_c, expected):
    triangle = Triangle(side_a, side_b, side_c)
    assert triangle.is_right_angled() == expected
