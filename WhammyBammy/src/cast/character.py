from common.domain_object import DomainObject

class Character(DomainObject):
    '''
    Has state about where it is.
    Has methods like fly, zoom, that send certain state attributes and return stage directions
    Also has appearance.  Like flying/talking which maps to images.
    '''

    def __init__(self, location):
        self.location = location
        #orientation ()
        #direction facting
    
    def __eq__(self, other):
        return isinstance(other, self.__class__)
    
    
    def __hash__(self):
        return 1 #todo: need to know which one