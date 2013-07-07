from preproduction.screenplay import Screenplay

class Presenter(object):

    def __init__(self, view):
        self.model = Screenplay.construct()
        self.view = view
        
    def initialize(self):
        self.view.show_scene(self.model.current_scene)
