import pytest
from hw2.src.Circle import *
from hw2.src.Square import *
from hw2.src.Rectangle import *
from hw2.src.Triangle import *


@pytest.mark.parametrize('side_a, perimeter, area',
                         [
                             (3, 18.84955592153876, 28.274333882308138),
                             (10, 62.83185307179586, 314.1592653589793),
                         ])
def test_circle(side_a, perimeter, area):
    c = Circle(side_a)
    assert c.name == 'Circle'
    assert c.get_area() == area
    assert c.get_perimeter() == perimeter


@pytest.mark.parametrize('side_a', [-5, 0])
def test_circle_negative(side_a):
    with pytest.raises(ValueError):
        Circle(side_a)


def test_figure_add_area():
    circle = Circle(3)
    square = Square(5)
    triangle = Triangle(3, 4, 5)
    rectangle = Rectangle(4, 5)
    assert square.add_area(square) == 50
    assert circle.add_area(rectangle) == 48.27433388230814
    assert circle.add_area(triangle) == 34.27433388230814
