from direction.movement import Movement
from common.coordinate import Coordinate
from common.domain_object import DomainObject

class StageDirection(DomainObject):
    """
    Has all the attributes that are needed to create a QGraphicsItemAnimation
    Has factory methods like walk, fly, etc
    
    """
    
    def __init__(self, start, end, character, movements):
        self.start = start
        self.end = end
        self.character = character
        self.movements = movements

    @property
    def duration(self):
        return self.end - self.start
    
    @classmethod
    def walk_left(cls, character, start, end):
        start_coordinate = character.location
        end_location = character.location - Coordinate(x=500)
        character.location = end_location
        movements = [Movement(step=0, coordinate=start_coordinate),
                     Movement(step=1, coordinate=end_location) ]
        return StageDirection(movements=movements,
                              character = character,
                              start=start,
                              end=end)
                                              
    
    
