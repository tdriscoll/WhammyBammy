from preproduction.screenplay import Screenplay

class Presenter(object):

    def __init__(self, view):
        self.model = Screenplay()
        self.view = view
        
    def initialize(self):
        self.bind_events()
        self.load_from_model()
        
    def bind_events(self):
        self.view.on_key_event = self.handle_key_event
        self.view.on_directions_finished = self.handle_directions_finished
    
    def handle_key_event(self, key_index):
        self.load_from_model()
        
    def load_from_model(self):
        scene = self.model.get_new_scene()
        if scene:
            self.view.init_scene(self.model.current_scene)
        
        directions = self.model.get_new_directions()
        if directions:
            self.view.load_directions(directions)
        
    def handle_directions_finished(self):
        self.model.directions_finished = True
