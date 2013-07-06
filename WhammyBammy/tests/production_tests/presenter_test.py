import unittest
from mock import Mock
from production.presenter import Presenter
from preproduction.scene import Scene

class PresenterTest(unittest.TestCase):


    def test_initialize_the_first_scene(self):
        view = Mock()
        sp = Presenter(view)
        sp.initialize()
        
        view.show_scene.assert_called_with(Scene(scene_number=1))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()