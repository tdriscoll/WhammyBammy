import unittest
from preproduction.screenplay import Screenplay

class ScreenplayTest(unittest.TestCase):


    def test_can_construct_starting_at_scene1(self):
        sp = Screenplay.construct()
        self.assertEqual(1, sp.current_scene.scene_number)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()