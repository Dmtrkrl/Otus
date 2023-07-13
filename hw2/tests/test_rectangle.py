import pytest
from hw2.src.Rectangle import *
from hw2.src.Triangle import *
from hw2.src.Square import *
from hw2.src.Circle import *


@pytest.mark.parametrize('side_a, side_b, perimeter, area',
                         [
                             (4, 5, 18, 20),
                             (10, 20, 60, 200),
                         ])
def test_rectangle(side_a, side_b, perimeter, area):
    r = Rectangle(side_a, side_b)
    assert r.name == 'Rectangle'
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter


@pytest.mark.parametrize('side_a, side_b',
                         [
                             (-1, 2),
                             (0, 20),
                         ])
def test_rectangle_negative(side_a, side_b):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)


def test_figure_add_area():
    rectangle = Rectangle(4, 5)
    triangle = Triangle(3, 4, 5)
    square = Square(5)
    circle = Circle(3)
    assert rectangle.add_area(triangle) == 26
    assert rectangle.add_area(square) == 45
    assert rectangle.add_area(circle) == 48.27433388230814
