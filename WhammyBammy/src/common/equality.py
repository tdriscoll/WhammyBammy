
def dict_equality(self, other):
    if not isinstance(other, self.__class__):
        return False
    return self.__dict__ == other.__dict__
        