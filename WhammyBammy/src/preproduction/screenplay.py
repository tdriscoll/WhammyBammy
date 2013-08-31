from preproduction.screenwriter import Screenwriter

class Screenplay(object):

    def __init__(self):
        self.directions_finished = True
        self.current_scene_number = 0
        self.current_scene= None
        self.screenwriter = Screenwriter()

    @property
    def current_scene_is_finished(self):
        return not self.current_scene or self.current_scene.is_finished
    
    def get_new_scene(self):
        if self.current_scene_is_finished:
            self.current_scene_number+= 1
            self.current_scene = self.screenwriter.build_scene(self.current_scene_number)
            return self.current_scene
    
    def get_new_directions(self):
        if self.directions_finished:
            self.directions_finished = False
            return self.current_scene.next()
