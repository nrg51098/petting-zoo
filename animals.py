# import the python datetime module to help us create a timestamp
from SnakePit.snakePit import SnakePit
from Wetlands.wetlands import Wetlands
from Donkey import Donkey
from Cobra import Cobra
from Copperhead import Copperhead
from Goat import Goat
from Goldfish import Goldfish
from Lion import Lion
from Lizard import Lizard
from Llama import Llama
from Mallard import Mallard
from Ratsnake import Ratsnake
from Shark import Shark
from Snipper import Snipper
from Tiger import Tiger
from Whale import Whale
from Octopus import Octopus

from PettingZoo import PettingZoo


aby = Donkey("aby", "shouting donkey", "morning", "muddy water")
boby = Llama("boby", "domestic llama", "afternoon", "llama chow")
carin = Goat("carin", "green goat", "night", "grass")
duster = Tiger("duster", "roaring tiger", "evening", "meat")
eric = Lion("eric", "sleeping lion", "morning", "tender meat")
fast = Copperhead("fast", "cold copperhead", "afternoon", "rats")
gordon = Ratsnake("gordon", "shattering ratsnake", "night", "tasty rat")
harish = Cobra("harish", "short cobra", "evening", "big rat")
ivan = Lizard("ivan", "active lizard", "evening", "butterfly")
jay = Snipper("jay", "redish snipper", "night", "bugs")
kumar = Mallard("kumar", "dancing mallard", "morning", "fish eggs")
lora = Goldfish("lora", "swimming goldfish", "night", "mudd bugs")
meter = Octopus("meter", "jumping octopus", "afternoon", "salty bugs")
nancy = Shark("nancy", "hunting shark", "afternoon", "fish")
octus = Whale("octus", "running whale", "morning", "big fish")

# print(f'{aby.name} the {aby.species} is available to pet during the {aby.shift} shift.')
# prints Roberto the alpaca is available to pet during the midday shift.

# miss_fuzz = Llama("Miss Fuzz", "domestic llama", "morning", "Llama Chow" )
# print(miss_fuzz)
# print(miss_fuzz.feed())

varmint_village = PettingZoo("Varmint Village")
varmint_village.add(aby)
varmint_village.add(boby)
varmint_village.add(carin)
varmint_village.add(duster)
varmint_village.add(eric)

slither_inn = SnakePit("Swimming bodies")
slither_inn.add(fast)
slither_inn.add(gordon)
slither_inn.add(harish)
slither_inn.add(ivan)
slither_inn.add(jay)


swimming_bodies = Wetlands("Slither Inn")
swimming_bodies.add(kumar)
swimming_bodies.add(lora)
swimming_bodies.add(meter)
swimming_bodies.add(nancy)
swimming_bodies.add(octus)

# name, species, shift and food
print (f'{varmint_village.attraction_name} is here you"ll find cute and fuzzy critters to cuddle, like')
for animal in varmint_village.animals:
    print(f'{animal.name} the {animal.species}')

print (f'{slither_inn.attraction_name} is here you"ll find crawling critters, like')
for animal in slither_inn.animals:
    print(f'{animal.name} the {animal.species}')

print (f'{swimming_bodies.attraction_name} is here you"ll find dancing and jumping critters, like')
for animal in swimming_bodies.animals:
    print(f'{animal.name} the {animal.species}')