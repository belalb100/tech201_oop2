# Inheretence

from animal import Animal

class Reptile(Animal): # Our reptile will inherent variables from our animal.py, but we can change it's methods.

    def __init__(self):
        super().__init__()  # Super here is a keyword
        self.cold_blooded = True
        self.tetrapod = None
        self.heart_chambers = [3, 4]
        self.amniotic_eggs = None

    def seek_heat(self):
        print("It's chilly outside, where is the sun.")

    def hunt(self):
        print("Wait, wait pounce.")
    def use_venom(self):
        print("If I have to use it I will.")

    def attract_through_scent(self):
        print("Time to spray some.")


jeremy_the_reptile = Reptile()

jeremy_the_reptile.breathe()
jeremy_the_reptile.hunt()
jeremy_the_reptile.eat()

