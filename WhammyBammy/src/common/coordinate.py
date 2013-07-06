from common.domain_object import DomainObject

class Coordinate(DomainObject):
    
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        
    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return Coordinate(self.x - other.x, self.y - other.y, self.z - other.z)
        
ORIGIN = Coordinate(0, 0, 0)
STAGE_LEFT = Coordinate(1000, 0, 0)