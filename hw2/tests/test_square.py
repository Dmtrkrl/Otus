import pytest
from hw2.src.Square import *
from hw2.src.Triangle import *
from hw2.src.Rectangle import *
from hw2.src.Circle import *

@pytest.mark.parametrize('side_a, perimeter, area',
                         [
                             (4, 16, 16),
                             (10, 40, 100),
                         ])
def test_square(side_a, perimeter, area):
    s = Square(side_a)
    assert s.name == 'Square'
    assert s.get_area() == area
    assert s.get_perimeter() == perimeter


@pytest.mark.parametrize('side_a', [-5, 0])
def test_square_negative(side_a):
    with pytest.raises(ValueError):
        Square(side_a)


def test_figure_add_area():
    square = Square(5)
    triangle = Triangle(3, 4, 5)
    rectangle = Rectangle(4, 5)
    circle = Circle(3)
    assert square.add_area(triangle) == 31
    assert square.add_area(rectangle) == 45
    assert square.add_area(circle) == 53.27433388230814
