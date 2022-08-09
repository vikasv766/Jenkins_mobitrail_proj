from source_code import Rectangle, Square
import unittest


# The test based on Unit test module
# ---------------------------------------------------------------------------------------------
class TestGetAreaRectangle(unittest.TestCase):
    def runTest(self):
        rectangle = Rectangle(3, 5)
        self.assertEqual(rectangle.get_area(), 15,
                         "Incorrect Area of Rectangle")


# ---------------------------------------------------------
class TestGetAreaSquare(unittest.TestCase):
    def runTest(self):
        square = Square(4)
        self.assertEqual(square.get_area(), 16, "Incorrect Area of Square")

# ----------------------------------------------------------------------------------------------------


# This code is to run the test:
unittest.main()
