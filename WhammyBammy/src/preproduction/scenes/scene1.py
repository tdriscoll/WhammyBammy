from preproduction.scene import Scene
from common.lazy_property import LazyProperty
from cast.casting import Casting
from common.coordinate import Coordinate


class Scene1(object):
    
    @LazyProperty
    def protagonist(self):
        return Casting.create_protagonist(Coordinate(600, 50, 0))

    @LazyProperty
    def antagonist(self):
        return Casting.create_antagonist(Coordinate(-500, 150, 0))
    
    def wait_for_audience(self):
        self.protagonist.current_time = 0
        self.antagonist.current_time = 0


    def build_scene(self):
        sc = Scene(scene_number = 1)
        
        sc.stage_directions.append(self.protagonist.zoom_in(duration = 5000))
        sc.stage_directions.append(self.protagonist.speak("La te da te da."))
        sc.stage_directions.append(self.wait_for_audience())
        sc.stage_directions.append(self.protagonist.walk_left(speed=2, distance = 500))
        sc.stage_directions.append(self.protagonist.speak("Ho hum"))
        sc.stage_directions.append(self.wait_for_audience())
        sc.stage_directions.append(self.protagonist.walk_right(speed=2, distance = 400))
        sc.stage_directions.append(self.protagonist.speak("Doodely de ta dum."))
        sc.stage_directions.append(self.wait_for_audience())
        #         
        sc.stage_directions.append(self.antagonist.walk_right(speed= 5, distance = 500))
        sc.stage_directions.append(self.antagonist.speak("READING IS HARD!"))
        sc.stage_directions.append(self.wait_for_audience())
         
        sc.stage_directions.append(self.protagonist.speak("AHHHHhhhH!"))
        sc.stage_directions.append(self.wait_for_audience())
         
        sc.stage_directions.append(self.protagonist.about_face())
        sc.stage_directions.append(self.protagonist.walk_right(speed=1, distance =  1000))
        
        self.antagonist.idle(duration=100)
        sc.stage_directions.append(self.antagonist.walk_right(speed= 3, distance = 1500))
        return sc
        
def get_scene():
    return Scene1().build_scene()