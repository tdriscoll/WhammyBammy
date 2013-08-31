import unittest
from preproduction.screenplay import Screenplay
from preproduction.screenwriter import Screenwriter
from preproduction.scene import Scene
from direction.stage_direction import StageDirection
from cast.casting import Casting
from common.coordinate import ORIGIN
from direction.movement import Movement

class ScreenplayTest(unittest.TestCase):

    def setUp(self):
        self.scene1 = Screenwriter().build_scene(1)
        self.scene1.next()
        self.sp = Screenplay()
        self.sp.get_new_scene()
        self.sp.get_new_directions()
    
    def test_can_construct_starting_at_scene1(self):
        self.assertEqual(1, self.sp.current_scene.scene_number)

    def test_get_nothing_in_middle_of_scene(self):
        self.assertEquals(None, self.sp.get_new_scene())
        self.assertEquals(None, self.sp.get_new_directions())
        self.assertEquals(self.sp.directions_finished, False)

    def test_get_next_directions_on_key_press(self):
        
        self.sp.directions_finished = True
        self.assertEquals(None, self.sp.get_new_scene())
        actual = self.sp.get_new_directions()
        self.assertEquals(self.sp.directions_finished, False)
        self.assertEquals(self.scene1.next(), actual)
        
    def test_get_next_scene_when_directions_finished(self):
        scene = Scene(scene_number = 1)
        scene.stage_directions = [StageDirection(start = 0, end = 10, character = Casting.create_antagonist(ORIGIN), movements = [Movement(step= 1, coordinate = ORIGIN, xscale = -1, yscale =1)])]
        self.sp.current_scene = scene
        self.sp.directions_finished = True
        self.sp.get_new_directions()
        self.sp.directions_finished = True
        actual = self.sp.get_new_scene()
        expected = Scene(scene_number=2)
        self.assertEquals(expected, actual)
        self.assertEquals(expected, self.sp.current_scene)
        self.assertTrue(self.sp.get_new_directions() is not None)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()