from common.domain_object import DomainObject

class Movement(DomainObject):
    """
    Has all the attributes that are needed to create a QGraphicsItemAnimation
    Has factory methods like walk, fly, etc
    
    """
    
    def __init__(self, step, coordinate, rotation=None):
        self.step = step
        self.coordinate = coordinate
        self.rotation = rotation
        #TODO: translation & sheear?
    
        