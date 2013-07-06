from common.equality import dict_equality

class DomainObject(object):
    
    __eq__ = dict_equality
    
    def __str__(self):
        return "{klass}({dunder_dict})".format(klass = self.__class__.__name__, 
                                               dunder_dict = self.__dict__)

    __repr__ = __str__
