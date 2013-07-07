import unittest
from direction.stage_direction import StageDirection
from direction.movement import Movement
from common.coordinate import Coordinate, ORIGIN
from cast.character import Character


class StageDirectionTest(unittest.TestCase):


    def test_can_calculate_duration(self):
        movement = Movement(step=0.5, coordinate=ORIGIN, rotation=350)
        sd = StageDirection(start=500, end=1200, movements=[movement], character = None)
        self.assertEquals(700, sd.duration)
        


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
