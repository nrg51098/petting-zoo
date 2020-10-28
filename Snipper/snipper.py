from datetime import date

class Snipper:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.walking = True
        self.date_added = date.today()
