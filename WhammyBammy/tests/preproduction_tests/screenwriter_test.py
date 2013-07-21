import unittest
from preproduction.screenwriter import Screenwriter
from preproduction.scene import Scene


class ScreenwriterTest(unittest.TestCase):


    def test_building_scenes_with_directions_until_end(self):
        sw = Screenwriter()
        scene_number = 1
        for _ in xrange(100): #no more than 100 scenes
            scene_number += 1
            actual = sw.build_scene(scene_number = scene_number)
            if actual is None:
                return
            expected = Scene(scene_number = scene_number)
            self.assertEquals(expected, actual)
            self.assertTrue(len(actual.stage_directions) > 1)
            scene_number += 1
        self.fail("Should not have more scenes")
        
        
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()