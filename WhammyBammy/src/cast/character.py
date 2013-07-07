from common.domain_object import DomainObject
from common.coordinate import Coordinate
from direction.movement import Movement
from direction.stage_direction import StageDirection

class Character(DomainObject):
    '''
    Has state about where it is.
    Has methods like fly, zoom, that send certain state attributes and return stage directions
    Also has appearance.  Like flying/talking which maps to images.
    '''

    def __init__(self, location):
        self.current_location = location
        self.current_time = 0
        #orientation ()
        #direction facting
    
    def __eq__(self, other):
        return isinstance(other, self.__class__)
    
    
    def __hash__(self):
        return 1 #todo: need to know which one
    
    
    def idle(self, duration):
        self.current_time += duration
    
    def walk_left(self, duration):
        start_coordinate = self.current_location
        end_location = start_coordinate - Coordinate(x=500)
        self.current_location = end_location
        movements = [Movement(step=0, coordinate=start_coordinate),
                     Movement(step=1, coordinate=end_location) ]
        direction =  StageDirection(movements=movements,
                              character = self,
                              start=self.current_time,
                              end=self.current_time + duration)
        self.current_time = direction.end
        return direction
    
    def zoom_in(self, duration):
        movements = [Movement(step=0, rotation=0, xscale = -0.1, yscale = 0.1, coordinate=self.current_location),
                     Movement(step=0.3, rotation=30, xscale = -0.3, yscale = 0.3, coordinate=self.current_location),
                     Movement(step=1, rotation=0, xscale = -0.7, yscale = 0.7, coordinate=self.current_location),
                    ]
        direction =  StageDirection(movements=movements,
                              character = self,
                              start=self.current_time,
                              end=self.current_time + duration)
        self.current_time = direction.end
        return direction