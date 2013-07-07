from common.domain_object import DomainObject
from common.coordinate import Coordinate
from direction.movement import Movement
from direction.stage_direction import StageDirection

class Character(DomainObject):
    '''
    Also has appearance.  Like flying/talking which maps to images.
    '''

    def __init__(self, name, location, image):
        self.name = name
        self.current_location = location
        self.current_time = 0
        self.image = image
        #orientation ()
        #direction facting
    
    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.name == other.name
    
    def __hash__(self):
        return hash(self.name)
    
    def idle(self, duration):
        self.current_time += duration
    
    def walk_left(self, duration):
        movements = [Movement(step=0, coordinate=self.current_location),
                     Movement(step=1, coordinate=self.current_location - Coordinate(x=500)) ]
        return self._directions_from_movements(movements, duration)
    
    def zoom_in(self, duration):
        movements = [Movement(step=0, rotation=0, xscale = -0.1, yscale = 0.1, coordinate=self.current_location),
                     Movement(step=0.3, rotation=30, xscale = -0.3, yscale = 0.3, coordinate=self.current_location),
                     Movement(step=1, rotation=0, xscale = -0.7, yscale = 0.7, coordinate=self.current_location),
                    ]
        return self._directions_from_movements(movements, duration)

    
    def _directions_from_movements(self, movements, duration):
        direction =  StageDirection(movements=movements,
                                    character = self,
                                    start=self.current_time,
                                    end=self.current_time + duration)
        self.current_time = direction.end
        self.current_location = movements[-1].coordinate
        return direction