import unittest
from preproduction.screenwriter import Screenwriter
from preproduction.scene import Scene


class ScreenwriterTest(unittest.TestCase):


    def test_building_scene1(self):
        sw = Screenwriter()
        expected = Scene(scene_number = 1)
        actual = sw.build_scene(scene_number = 1)
        self.assertEquals(expected, actual)
        
    def test_no_more_scenes_to_build(self):
        sw = Screenwriter()
        self.assertEquals(None, sw.build_scene(scene_number = 2))
        
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()