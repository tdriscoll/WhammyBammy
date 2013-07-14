from preproduction.screenplay import Screenplay

class Presenter(object):

    def __init__(self, view):
        self.model = Screenplay.construct()
        self.view = view
        self.directions_finished = False
        
    def initialize(self):
        self.view.on_key_event = self.handle_key_event
        self.view.on_directions_finished = self.handle_directions_finished
        self.view.init_scene(self.model.current_scene)
        self.view.load_directions(self.model.current_scene.next())
        
    def handle_key_event(self, key_index):
        #TODO: test
        if self.directions_finished:
            self.directions_finished = False
            self.view.load_directions(self.model.current_scene.next())
        
    def handle_directions_finished(self):
        self.directions_finished = True
