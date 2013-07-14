import unittest
from mock import Mock
from production.presenter import Presenter
from preproduction.screenwriter import Screenwriter

class PresenterTest(unittest.TestCase):
    
    def setUp(self):
        self.scene1 = Screenwriter().build_scene(1)
        self.view = Mock()
        self.presenter = Presenter(self.view)
        
    def test_initialize_the_first_scene(self):
        self.presenter.initialize()
        self.view.init_scene.assert_called_with(self.scene1)
        self.view.load_directions.assert_called_with(self.scene1.next())

    def test_key_press_does_nothing_in_middle_of_scene(self):
        sp = Presenter(view=None)
        sp.handle_key_event(key_index=56)
        self.assertEquals(sp.directions_finished, False)

    def test_load_next_directions_on_key_press(self):
        self.presenter.directions_finished = True
        self.presenter.handle_key_event(key_index=56)
        self.assertEquals(self.presenter.directions_finished, False)
        self.view.load_directions.assert_called_with(self.scene1.next())
        
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()