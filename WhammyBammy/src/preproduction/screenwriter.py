from cast.casting import Casting
from common.coordinate import ORIGIN, STAGE_LEFT, Coordinate
from preproduction.scene import Scene

class Screenwriter(object):


    def build_scene(self, scene_number):
        if scene_number != 1:
            return
        protagonist = Casting.create_protagonist(Coordinate(1000, 100, 0))
        sc = Scene(scene_number = scene_number)
        sc.stage_directions.append(protagonist.zoom_in(duration = 5000))
        sc.stage_directions.append(protagonist.walk_left(duration= 1000))
        return sc