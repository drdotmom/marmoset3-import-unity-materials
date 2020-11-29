class EmptyStore():

    def __init__(self):

        self.path = None
        self.store = None
        #self.rgb = [1.0, 1.0, 1.0]
        #self.rgba = [1.0, 1.0, 1.0, 0.0]
        #self.a = 0.0


class FIELD(object):

    def __init__(self, field):

        self.name = field[0]
        self.type = field[1]
        self.store = EmptyStore()


class RGBA(object):

    def __init__(self, rgba):

        self.rgb = rgba[:-1]
        self.r = rgba[0]
        self.g = rgba[1]
        self.b = rgba[2]
        self.a = rgba[-1]
