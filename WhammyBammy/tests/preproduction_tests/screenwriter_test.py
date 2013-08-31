import unittest
from preproduction.screenwriter import Screenwriter, NoMoreScenesException

class ScreenwriterTest(unittest.TestCase):
    
    def setUp(self):
        self.sw = Screenwriter()
        self.sw.scene_package_loc = "test_framework.scenes"
    
    def test_building_scene1_returns_correct_scene_number(self):
        scene = self.sw.build_scene(1)
        self.assertEquals(1, scene.scene_number)

    def test_building_scene2_returns_correct_scene_number(self):
        scene = self.sw.build_scene(2)
        self.assertEquals(2, scene.scene_number)
        
    def test_can_point_do_different_scenes(self):
        scene = self.sw.build_scene(1)
        self.assertEquals("Testing is important", scene.stage_directions[0].character.text)
    
    def test_building_scene_that_does_exist_raises_exception(self):
        self.assertRaises(NoMoreScenesException, self.sw.build_scene, 3)
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()