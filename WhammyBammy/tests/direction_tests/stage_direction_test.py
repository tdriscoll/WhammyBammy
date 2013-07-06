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
        
    def test_can_start_by_walking_left(self):
        character = Character(location=ORIGIN)
        direction = StageDirection.walk_left(character, start=0, end=1000)
        expected = StageDirection(movements=[Movement(step=0, coordinate=ORIGIN),
                                             Movement(step=1, coordinate=Coordinate(x=-500)), ],
                                  start=0,
                                  end=1000, 
                                  character = character)
        self.assertEquals(expected, direction)
        
    def test_can_walk_even_father_left(self):
        character = Character(location=ORIGIN)
        StageDirection.walk_left(character, start=0, end=1000)
        direction = StageDirection.walk_left(character, start=1200, end=2000)
        expected = StageDirection(movements=[Movement(step=0, coordinate=Coordinate(x=-500)),
                                             Movement(step=1, coordinate=Coordinate(x=-1000)), ],
                                  start=1200,
                                  end=2000, 
                                  character = character)
        self.assertEquals(expected, direction)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
