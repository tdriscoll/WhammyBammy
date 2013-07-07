import unittest
from common.coordinate import ORIGIN, Coordinate
from cast.character import Character
from direction.stage_direction import StageDirection
from direction.movement import Movement
from common.equality import DictEqualityDebug

class CharacterTest(unittest.TestCase):
    
    def setUp(self):
        self.character = Character(name = "Test Me", location=ORIGIN, image = "who cares")
    
    def test_can_idle(self):
        self.character.idle(159)
        self.assertEqual(ORIGIN, self.character.current_location)
        self.assertEqual(159, self.character.current_time)
        self.character.idle(3)
        self.assertEqual(162, self.character.current_time)

    def test_can_start_by_walking_left(self):
        actual = self.character.walk_left(duration=1000)
        expected = StageDirection(start=0, end=1000,character = self.character,
                                  movements=[Movement(step=0, coordinate=ORIGIN),
                                             Movement(step=1, coordinate=Coordinate(x=-500)), ],
                                  )
        self.assertEquals(expected, actual)
        
        
    def test_can_walk_even_father_left(self):
        self.character.walk_left(duration=1000)
        actual = self.character.walk_left(duration=2200)
        expected = StageDirection(start=1000, end=3200, character = self.character,
                                  movements=[Movement(step=0, coordinate=Coordinate(x=-500)),
                                             Movement(step=1, coordinate=Coordinate(x=-1000)), ],
                                  )
        with DictEqualityDebug():
            self.assertEquals(expected, actual)
            
            
    def test_can_fly_in(self):
        actual = self.character.zoom_in(duration=1000)
        expected = StageDirection(start=0, end=1000, character = self.character, 
                                  movements=[Movement(step=0, rotation=0, xscale = -0.1, yscale= 0.1, coordinate = ORIGIN),
                                             Movement(step=0.3, rotation=30, xscale = -0.3, yscale= 0.3, coordinate = ORIGIN),
                                             Movement(step=1, rotation=0, xscale = -0.7, yscale= 0.7, coordinate = ORIGIN),
                                             ],
                      )
        with DictEqualityDebug():
            self.assertEquals(expected, actual)
            
    def test_characters_are_hashable_and_equalable(self):
        bob = Character(location=ORIGIN, name = "Bob" , image = "x")
        sally = Character(location=ORIGIN, name = "Sally", image = "x")
        characters = set([bob, sally])
        self.assertEqual(2, len(characters))
        characters.add(Character(location=ORIGIN, name = "Bob", image = "x"))
        self.assertEqual(2, len(characters))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()