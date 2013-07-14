from cast.casting import Casting
from common.coordinate import ORIGIN, STAGE_LEFT, Coordinate
from preproduction.scene import Scene
from cast.character import Character
from common.lazy_property import LazyProperty

class Screenwriter(object):

    @LazyProperty
    def protagonist(self):
        return Casting.create_protagonist(Coordinate(600, 50, 0))

    @LazyProperty
    def antagonist(self):
        return Casting.create_antagonist(Coordinate(-500, 150, 0))
    
    def wait_for_audience(self):
        self.protagonist.current_time = 0
        self.antagonist.current_time = 0
    
    def build_scene(self, scene_number):
        if scene_number != 1:
            return
        sc = Scene(scene_number = scene_number)
        
        sc.stage_directions.append(self.protagonist.zoom_in(duration = 5000))
        sc.stage_directions.append(self.protagonist.speak("La te da te da."))
        sc.stage_directions.append(self.wait_for_audience())
        sc.stage_directions.append(self.protagonist.walk_left(speed=2, distance = 500))
        sc.stage_directions.append(self.protagonist.speak("Ho hum"))
        sc.stage_directions.append(self.wait_for_audience())
        sc.stage_directions.append(self.protagonist.walk_right(speed=2, distance = 400))
        sc.stage_directions.append(self.protagonist.speak("Doodely de ta dum."))
        sc.stage_directions.append(self.wait_for_audience())
        
        sc.stage_directions.append(self.antagonist.walk_right(speed= 5, distance = 500))
        sc.stage_directions.append(self.antagonist.speak("READING IS HARD!"))
        sc.stage_directions.append(self.wait_for_audience())
        
        sc.stage_directions.append(self.protagonist.speak("AHHHHhhhH!"))
        
        return sc