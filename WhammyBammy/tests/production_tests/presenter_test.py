import unittest
from mock import Mock
from production.presenter import Presenter
from preproduction.screenwriter import Screenwriter
from preproduction.scene import Scene

class PresenterTest(unittest.TestCase):
    
    def setUp(self):
        self.scene1 = Screenwriter().build_scene(1)
        self.scene2 = Screenwriter().build_scene(2)
        self.view = Mock()
        self.presenter = Presenter(self.view)
        self.presenter.model.directions_finished = False
        self.presenter.model.current_scene = self.scene1
        
        
    def test_initialize_the_first_scene(self):
        self.presenter.initialize()
        self.view.init_scene.assert_called_with(self.scene1)
        self.view.load_directions.assert_called_with(self.scene1.next())

    def test_key_press_does_nothing_in_middle_of_scene(self):
        presenter = Presenter(view=None)
        presenter.model.directions_finished = False
        presenter.model.current_scene = self.scene1
        presenter.handle_key_event(key_index=56)

    def test_load_next_directions_on_key_press(self):
        self.presenter.handle_directions_finished()
        self.presenter.handle_key_event(key_index=56)
        self.view.load_directions.assert_called_with(self.scene1.next())
        
    def test_get_next_scene_on_key_press(self):
        scene = Scene(scene_number = 1)
        self.presenter.model.current_scene = scene
        self.presenter.handle_directions_finished()
        
        self.presenter.handle_key_event(key_index = 100)

        self.view.init_scene.assert_called_with(self.scene2)
        self.view.load_directions.assert_called_with(self.scene2.next())
        
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()