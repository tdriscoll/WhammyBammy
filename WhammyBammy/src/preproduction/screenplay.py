from preproduction.screenwriter import Screenwriter

class Screenplay(object):

    def __init__(self):
        self.current_scene = None

    @classmethod
    def construct(cls):
        sp = Screenplay()
        sp.current_scene = Screenwriter().build_scene(1)
        return sp