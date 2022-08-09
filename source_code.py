
# import unittest
# # from unittest import TestCase


# Our code to be tested
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height


# rectangle = Rectangle(3, 4)
# AreaOfRectangle = rectangle.get_area()
# print("AreaOfRectangle--->", AreaOfRectangle)

# --------------------------------------------------------------------------------------------

class Square:
    def __init__(self, a1):
        self.a1 = a1

    def get_area(self):
        return self.a1**2

    def set_side(self, side):
        self.side = side


# square = Square(3)
# AreaOfSquare = square.get_area()
# print("AreaOfSquare-->", AreaOfSquare)
