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
        actual = self.character.walk_left(speed=3, distance=500)
        expected = StageDirection(start=0, end=1500,character = self.character,
                                  movements=[Movement(step=0, coordinate=ORIGIN),
                                             Movement(step=1, coordinate=Coordinate(x=-500)), ],
                                  )
        self.assertEquals(expected, actual)

    def test_can_walking_right(self):
        actual = self.character.walk_right(speed=5, distance=200)
        expected = StageDirection(start=0, end=1000, character = self.character,
                                  movements=[Movement(step=0, coordinate=ORIGIN),
                                             Movement(step=1, coordinate=Coordinate(x=200)), ],
                                  )
        self.assertEquals(expected, actual)
        
        
    def test_can_walk_even_father_left(self):
        self.character.walk_left(distance=50, speed = 3)
        actual = self.character.walk_left(distance=500, speed = 1)
        expected = StageDirection(start=150, end=650, character = self.character,
                                  movements=[Movement(step=0, coordinate=Coordinate(x=-50)),
                                             Movement(step=1, coordinate=Coordinate(x=-550)), ],
                                  )
        with DictEqualityDebug():
            self.assertEquals(expected, actual)
            
            
    def test_can_fly_in(self):
        actual = self.character.zoom_in(duration=1000)
        expected = StageDirection(start=0, end=1000, character = self.character, 
                                  movements=[Movement(step=0, rotation=0, xscale = 0.1, yscale= 0.1, coordinate = ORIGIN),
                                             Movement(step=0.3, rotation=30, xscale = 0.3, yscale= 0.3, coordinate = ORIGIN),
                                             Movement(step=1, rotation=0, xscale = 1, yscale= 1, coordinate = ORIGIN),
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
        
    def test_can_speak(self):
        actual = self.character.speak("How about them apples?")
        expected_coord = Coordinate(x=100)
        text = Character(name= "Test Me- Line 1", location = expected_coord, image = None)
        expected = StageDirection(start=0, end=1, character = text, 
                                  movements=[Movement(step=0, coordinate = expected_coord),],
                                  )
        with DictEqualityDebug():
            self.assertEquals(expected, actual)
            self.assertEquals("How about them apples?", actual.character.text)

        
    def test_can_speak_from_the_right(self):
        self.character.current_location = Coordinate(x=800, y=40)
        actual = self.character.speak("Where's the beef?")
        expected_coord = Coordinate(x=400, y=25)
        text = Character(name= "Test Me- Line 1", location = expected_coord, image = None)
        expected = StageDirection(start=0, end=1, character = text, 
                                  movements=[Movement(step=0, coordinate = expected_coord),],
                                  )
        with DictEqualityDebug():
            self.assertEquals(expected, actual)
            self.assertEquals("Where's the beef?", actual.character.text)
            
    def test_can_speak_more_than_once(self):
        actual = self.character.speak("Knock Knock")
        self.assertEquals("Test Me- Line 1", actual.character.name)
        actual = self.character.speak("Aren't you glad I didn't say banana?")
        self.assertEquals("Test Me- Line 2", actual.character.name)
        
        
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()