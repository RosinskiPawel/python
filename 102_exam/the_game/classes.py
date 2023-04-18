class Player:
    def __init__(self, name, IQ_level):
        self.name = name
        self.IQ_level = IQ_level


class Items:
    def __init__(self, name, location):
        self.name = name
        self.location = location


class Knife(Items):
    def __init__(self, name, location, length):
        super().__init__(name, location)
        self.length = length


class Pencil(Items):
    def __init__(self, name, location):
        super().__init__(name, location)


class Table:
    def __init__(self, form, location):
        self.shape = form
        self.location = location


class Book:
    def __init__(self, art):
        self.art = art
