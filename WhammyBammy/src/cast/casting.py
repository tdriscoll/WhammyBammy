from cast.character import Character

class Casting(object):
    
    @classmethod
    def create_protagonist(cls, location):
        return Character(location)