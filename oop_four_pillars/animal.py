# Abstraction

class Animal:

    def __init__(self):
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breathe(self):
        print("One breath in and one breath out")

    def eat(self):
        print("nom nom nom")

    def procreate(self):
        print("Find a mate.")

    def move(self):
        print("Onwards and Upwards.")

cat = Animal()
cat.breathe()

# User just needs to no how to run the code and no how it works inside and outside.