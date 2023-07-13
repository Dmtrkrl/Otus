from hw2.src.Figure import *
import math


class Circle(Figure):
    def __init__(self, side_a):
        if side_a <= 0:
            raise ValueError(f'Can note create Square')
        self.side_a = side_a
        self.name = 'Circle'


    def get_area(self):
        return math.pi * self.side_a  ** 2


    def get_perimeter(self):
        return 2 * math.pi * self.side_a
