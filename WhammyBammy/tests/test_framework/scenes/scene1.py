from preproduction.scene import Scene
from common.lazy_property import LazyProperty
from cast.casting import Casting
from common.coordinate import Coordinate


class Scene1(object):
    
    @LazyProperty
    def protagonist(self):
        return Casting.create_protagonist(Coordinate(0, 0, 0))

    @LazyProperty
    def antagonist(self):
        return Casting.create_antagonist(Coordinate(0, 0, 0))
    
    def wait_for_audience(self):
        self.protagonist.current_time = 0
        self.antagonist.current_time = 0


    def build_scene(self):
        sc = Scene(scene_number = 1)
        
        sc.stage_directions.append(self.protagonist.speak("Testing is important"))
        sc.stage_directions.append(self.wait_for_audience())
        sc.stage_directions.append(self.protagonist.walk_left(speed=2, distance = 500))
        sc.stage_directions.append(self.antagonist.speak("Yes it is"))
        return sc
        
def get_scene():
    return Scene1().build_scene()