import unittest
from mock import Mock
from production.presenter import Presenter
from test_framework.scenes.scene1 import Scene1
from test_framework.scenes.scene2 import Scene2

class PresenterTest(unittest.TestCase):
    
    def setUp(self):
        self.view = Mock()
        
        self.presenter = Presenter(self.view)
        self.presenter.model.screenwriter.scene_package_loc = "test_framework.scenes"
        self.presenter.initialize()

        self.scene1 = Scene1().build_scene()
    
    def press_key_when_finished(self):
        self.presenter.handle_directions_finished()
        self.presenter.handle_key_event(key_index=101)
        
    def test_initialize_loads_the_first_scene(self):
        self.view.init_scene.assert_called_with(self.scene1)
        self.view.load_directions.assert_called_with(self.scene1.next())
        
    def test_key_press_does_nothing_in_middle_of_scene(self):
        presenter = Presenter(view=None)
        presenter.model.directions_finished = False
        presenter.model.current_scene = self.scene1
        presenter.handle_key_event(key_index=56)
 
    def test_on_key_press_load_the_next_set_of_directions(self):
        self.press_key_when_finished()
        self.scene1.next() #Discard scene
        self.view.load_directions.assert_called_with(self.scene1.next())
         
    def test_press_enough_keys_and_get_next_scene(self):
        scene2 = Scene2().build_scene()

        self.press_key_when_finished()
        self.view.reset_mock()
        self.press_key_when_finished()        
        
        self.view.init_scene.assert_called_with(scene2)
        self.view.load_directions.assert_called_with(scene2.next())
         
    def test_press_even_more_keys_and_app_quits(self):
        self.press_key_when_finished()
        self.press_key_when_finished()
        self.view.reset_mock()
        self.press_key_when_finished()        
        self.view.quit.assert_called_with()
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()