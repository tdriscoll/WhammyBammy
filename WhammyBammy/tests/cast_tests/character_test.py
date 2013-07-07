import unittest
from common.coordinate import ORIGIN, Coordinate
from cast.character import Character
from direction.stage_direction import StageDirection
from direction.movement import Movement
from common.equality import DictEqualityDebug

class CharacterTest(unittest.TestCase):

    def test_can_idle(self):
        character = Character(location=ORIGIN)
        character.idle(159)
        self.assertEqual(ORIGIN, character.current_location)
        self.assertEqual(159, character.current_time)
        character.idle(3)
        self.assertEqual(162, character.current_time)

    def test_can_start_by_walking_left(self):
        character = Character(location=ORIGIN)
        actual = character.walk_left(duration=1000)
        expected = StageDirection(start=0, end=1000,character = character,
                                  movements=[Movement(step=0, coordinate=ORIGIN),
                                             Movement(step=1, coordinate=Coordinate(x=-500)), ],
                                  )
        self.assertEquals(expected, actual)
        
        
    def test_can_walk_even_father_left(self):
        character = Character(location=ORIGIN)
        character.walk_left(duration=1000)
        actual = character.walk_left(duration=2200)
        expected = StageDirection(start=1000, end=3200, character = character,
                                  movements=[Movement(step=0, coordinate=Coordinate(x=-500)),
                                             Movement(step=1, coordinate=Coordinate(x=-1000)), ],
                                  )
        with DictEqualityDebug():
            self.assertEquals(expected, actual)
            
            
    def test_can_fly_in(self):
        character = Character(location=ORIGIN)
        actual = character.zoom_in(duration=1000)
        expected = StageDirection(start=0, end=1000, character = character, 
                                  movements=[Movement(step=0, rotation=0, xscale = -0.1, yscale= 0.1, coordinate = ORIGIN),
                                             Movement(step=0.3, rotation=30, xscale = -0.3, yscale= 0.3, coordinate = ORIGIN),
                                             Movement(step=1, rotation=0, xscale = -0.7, yscale= 0.7, coordinate = ORIGIN),
                                             ],
                      )
        with DictEqualityDebug():
            self.assertEquals(expected, actual)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()