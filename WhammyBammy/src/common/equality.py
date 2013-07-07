
class DictEquality(object):
    
    @staticmethod
    def equals(this, that):
        if not isinstance(that, this.__class__):
            return False
        return this.__dict__ == that.__dict__
        
class DictEqualityDebug(object):
    
    def __init__(self):
        self.save_dict_equality = DictEquality.equals
    
    @staticmethod
    def debug_dict_equality(this, that):
        if not isinstance(that, this.__class__):
            print "Diff class", this.__class__, that.__class__
            return False
        
        this_dict = this.__dict__
        that_dict = that.__dict__
        for key in set(this_dict.keys() + that_dict.keys()):
            if not this_dict.get(key) == that_dict.get(key):
                print ">>>", key, this_dict.get(key) , "!=",  that_dict.get(key)
        return this.__dict__ == that.__dict__
        
    def __enter__(self):
        DictEquality.equals = staticmethod(self.debug_dict_equality)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        DictEquality.equals = staticmethod(self.save_dict_equality)
        
        
dict_equality = lambda this, that: DictEquality.equals(this, that)