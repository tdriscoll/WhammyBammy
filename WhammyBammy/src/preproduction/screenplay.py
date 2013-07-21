from preproduction.screenwriter import Screenwriter
from common.lazy_property import LazyProperty

class Screenplay(object):

    def __init__(self):
        self.directions_finished = True
        self.current_scene = None
        self.current_scene_number = 0

    
    def get_new_scene(self):
        if self.current_scene.is_finished:
            self.current_scene_number+= 1
            self.current_scene = Screenwriter().build_scene(self.current_scene_number)
            return self.current_scene
    
    def get_new_directions(self):
        if self.directions_finished:
            self.directions_finished = False
            return self.current_scene.next()
