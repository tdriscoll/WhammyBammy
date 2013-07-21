from common.domain_object import DomainObject
from common.coordinate import Coordinate, ORIGIN, STAGE_LEFT
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
        self.text = None
        self.current_line_number = 0
        # orientation ()
        # direction facting
    
    def about_face(self):
        movements = [Movement(step=0, xscale=-1, yscale=1, coordinate=self.current_location),
                     Movement(step=1, xscale=-1, yscale=1, coordinate=self.current_location + Coordinate(x=500)),
                    ]
        return self._directions_from_movements(movements, duration=1)
    
    def speak(self, speaking_line):
        #TODO: this should not be a character.  multiple places in view treat text differently
        self.current_line_number+= 1
        y = max(self.current_location.y - 15, 0)
        x = 100 if self.current_location.x < 300 else 400
        loc = Coordinate(x, y)
        text = Character(name=self.name + "- Line %s" % self.current_line_number, location=loc, image=None)
        text.text = speaking_line
        return StageDirection(movements=[Movement(step=0, coordinate=loc)],
                                                character=text,
                                                start=self.current_time,
                                                end=self.current_time+1)
    
    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.name == other.name
    
    def __hash__(self):
        return hash(self.name)
    
    def idle(self, duration):
        # TODO: override for protagonist to bobble up and down (using function)
        return self.walk_to(duration, self.current_location)
    
    def walk_left(self, speed, distance):
        duration = speed * distance
        return self.walk_to(duration, self.current_location - Coordinate(x=distance))
    
    def walk_right(self, speed, distance):
        duration = speed * distance
        return self.walk_to(duration, self.current_location + Coordinate(x=distance))
    
    def walk_to(self, duration, end_coordinate):
        movements = [Movement(step=0, coordinate=self.current_location),
                     Movement(step=1, coordinate=end_coordinate) ]
        return self._directions_from_movements(movements, duration)
    
    def zoom_in(self, duration):
        movements = [Movement(step=0, rotation=0, xscale=0.1, yscale=0.1, coordinate=self.current_location),
                     Movement(step=0.3, rotation=30, xscale=0.3, yscale=0.3, coordinate=self.current_location),
                     Movement(step=1, rotation=0, xscale=1, yscale=1, coordinate=self.current_location),
                    ]
        return self._directions_from_movements(movements, duration)

    
    def _directions_from_movements(self, movements, duration):
        direction = StageDirection(movements=movements,
                                    character=self,
                                    start=self.current_time,
                                    end=self.current_time + duration)
        self.current_time = direction.end
        self.current_location = movements[-1].coordinate
        return direction
