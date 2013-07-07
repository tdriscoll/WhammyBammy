from cast.casting import Casting
from common.coordinate import ORIGIN, STAGE_LEFT, Coordinate
from preproduction.scene import Scene

class Screenwriter(object):


    def build_scene(self, scene_number):
        if scene_number != 1:
            return
        protagonist = Casting.create_protagonist(Coordinate(700, 100, 0))
        antagonist = Casting.create_antagonist(Coordinate(500, 0, 0))
        antagonist.idle(duration=1000)
        sc = Scene(scene_number = scene_number)
        sc.stage_directions.append(protagonist.zoom_in(duration = 5000))
        sc.stage_directions.append(antagonist.walk_left(duration= 1000))
        return sc