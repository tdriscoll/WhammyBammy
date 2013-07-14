from common.domain_object import DomainObject
from common.lazy_property import LazyProperty

class Scene(DomainObject):
    
    def __init__(self, scene_number):
        self.scene_number= scene_number
        self.stage_directions = []
        
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.scene_number == other.scene_number
    
    def next(self):
        return self.batches.next()
    
    @LazyProperty
    def batches(self):
        batch = []
        for stage_direction in self.stage_directions:
            if not stage_direction:
                yield batch
                batch = []
                continue
            batch.append(stage_direction)
        if batch:
            yield batch