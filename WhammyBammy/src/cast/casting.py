from cast.character import Character

class Casting(object):
    
    @classmethod
    def create_protagonist(cls, location):
        return Character(name = "Mothra", location=location, image = "protagonist.jpg")

    @classmethod
    def create_antagonist(cls, location):
        return Character(name = "Godzilla", location=location, image = "antagonist.jpg")