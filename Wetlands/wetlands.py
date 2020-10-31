class Wetlands:
    def __init__(self, name):
        self.attraction_name = name
        self.description = "wel critters to jump"
        self.animals = list()
        
    def add(self, animal):
        self.animals.append(animal)