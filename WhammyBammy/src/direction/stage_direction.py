from common.domain_object import DomainObject

class StageDirection(DomainObject):
    
    def __init__(self, start, end, character, movements):
        self.start = start
        self.end = end
        self.character = character
        self.movements = movements

    @property
    def duration(self):
        return self.end - self.start
    

    
    
                                              
    
    
