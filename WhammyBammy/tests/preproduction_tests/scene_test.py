import unittest
from preproduction.scene import Scene
from direction.stage_direction import StageDirection
from cast.casting import Casting
from common.coordinate import ORIGIN


class SceneTest(unittest.TestCase):


    def test_get_one_batch(self):
        character = Casting.create_antagonist(ORIGIN)
        s = Scene(scene_number = 8)
        s.stage_directions = [StageDirection(start = 0, end = 10, character = character, movements = "dancing"),
                              StageDirection(start = 10, end = 20, character = character, movements = "prancing")
                              ]
        self.assertFalse(s.is_finished)
        self.assertEquals(s.stage_directions, s.next())
        self.assertTrue(s.is_finished)

    def test_get_two_batches(self):
        character = Casting.create_antagonist(ORIGIN)
        directions1 = [StageDirection(start = 0, end = 10, character = character, movements = "dancing"),
                      StageDirection(start = 10, end = 20, character = character, movements = "prancing")]
        directions2 = [StageDirection(start = 0, end = 10, character = character, movements = ""),
                      StageDirection(start = 10, end = 20, character = character, movements = "prancing")
                      ]
        s = Scene(scene_number = 8)
        s.stage_directions = directions1 + [None] + directions2
        self.assertFalse(s.is_finished)
        self.assertEquals(directions1, s.next())
        self.assertFalse(s.is_finished)
        self.assertEquals(directions2, s.next())
        self.assertTrue(s.is_finished)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()