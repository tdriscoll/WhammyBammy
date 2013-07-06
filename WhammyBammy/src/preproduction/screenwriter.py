from cast.casting import Casting
from common.coordinate import ORIGIN, STAGE_LEFT
from direction.stage_direction import StageDirection
from preproduction.scene import Scene

class Screenwriter(object):


    def build_scene(self, scene_number):
        if scene_number != 1:
            return
        protagonist = Casting.create_protagonist(STAGE_LEFT)
        sc = Scene(scene_number = scene_number)
        sc.stage_directions.append(StageDirection.walk_left(protagonist, start = 0, end = 2000))
        sc.stage_directions.append(StageDirection.walk_left(protagonist, start = 3000, end = 4000))
        return sc