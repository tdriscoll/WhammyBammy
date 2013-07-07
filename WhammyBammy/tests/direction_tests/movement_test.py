import unittest
from direction.movement import Movement
from common.coordinate import Coordinate


class MovementTest(unittest.TestCase):


    def test_construct_movement(self):
        sd = Movement(step = 0.5, 
                    coordinate = Coordinate(0, 0, 0), 
                    rotation = 350, 
                    xscale = 0.5,
                    yscale = 0.5,
                    )


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()