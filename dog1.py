# Intialasation

# Relates to setting a particular data for an instance of a class.
# Instantiation -> Is the creation of an instance of an object.

class Dog:

    animal_kind = "canine"

    def __init__(self, name, colour):#User further down will have specify these things.
        self.animal_kind = "canine" # We have to add self in order to put in our class.
        self.name = name
        self.colour = colour

    def bark(self): #This is a method which is effectively a function.
        return "woof"


fido = Dog("Fido", "Brown") #Objects are under the class which is dog and fido is the object.

print(fido.name)
print(fido.colour)


# __init__