
class SnakePit:
    def __init__(self, name):
        self.attraction_name = name
        self.description = "crawling critters to scare"
        self.animals = list()

    def add(self, animal):
        self.animals.append(animal)