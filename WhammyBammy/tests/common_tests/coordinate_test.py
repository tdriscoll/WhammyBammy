import unittest
from common.coordinate import Coordinate


class CoordinateTest(unittest.TestCase):


    def test_add_coordinates(self):
        actual = Coordinate(x=1, y=2, z=3) + Coordinate(x=5, y=7, z=11)
        expected = Coordinate(x=6, y=9, z=14)
        self.assertEquals(expected, actual)

    def test_subtract_coordinates(self):
        actual = Coordinate(x=1, y=7, z=3) - Coordinate(x=5, y=2, z=11)
        expected = Coordinate(x=-4, y=5, z=-8)
        self.assertEquals(expected, actual)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()