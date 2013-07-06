from common.domain_object import DomainObject

class Scene(DomainObject):
    
    def __init__(self, scene_number):
        self.scene_number= scene_number
        self.stage_directions = []
        
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.scene_number == other.scene_number