from importlib import import_module

class NoMoreScenesException(Exception): pass

class Screenwriter(object):
    
    def __init__(self):
        self.scene_package_loc = "preproduction.scenes"
    
    def build_scene(self, scene_number):
        try:
            my_mod = import_module(self.scene_package_loc + ".scene" + str(scene_number))
        except ImportError:
            raise NoMoreScenesException("No more scenes :(")
        return my_mod.get_scene()
    
