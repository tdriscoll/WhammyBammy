from cast.casting import Casting
from common.coordinate import Coordinate
from preproduction.scene import Scene
from common.lazy_property import LazyProperty


class Scene2(object):

    @LazyProperty
    def protagonist(self):
        return Casting.create_protagonist(Coordinate(-100, 50, 0))

    @LazyProperty
    def antagonist(self):
        return Casting.create_antagonist(Coordinate(-500, 150, 0))
    
    def wait_for_audience(self):
        self.protagonist.current_time = 0
        self.antagonist.current_time = 0

    def build_scene(self):
        sc = Scene(scene_number = 2)
        
        sc.stage_directions.append(self.protagonist.about_face())
        sc.stage_directions.append(self.protagonist.walk_right(speed= 1, distance = 600))
        sc.stage_directions.append(self.protagonist.speak("AHHHHHHHHH!!!!"))
        sc.stage_directions.append(self.wait_for_audience())
        sc.stage_directions.append(self.protagonist.walk_right(speed= 2, distance = 1500))
        sc.stage_directions.append(self.wait_for_audience())
        return sc

def get_scene():
    return Scene2().build_scene()
    
