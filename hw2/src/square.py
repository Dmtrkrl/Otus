from hw2.src.Figure import *


class Square(Figure):
    def __init__(self, side_a):
        if side_a <= 0:
            raise ValueError(f'Can note create Square')
        self.side_a = side_a
        self.name = 'Square'

    def get_area(self):
        return self.side_a ** 2

    def get_perimeter(self):
        return 4 * self.side_a
