# Object Oriented Program

# Everything in OOP is an object and objects are modelled against real world objects.

# Classes are the templates we use to create objects.
# Classes are a way of bringing both data and functionality of our code together.

# Create a class

class Dog:

    animal_kind = "canine" #class variable/ attributes.

    def bark(self): # method - We always use SELF as this is what references the class.
        # print(self.animal_kind) # Self:look at the current self which is the dog class.
        return "woof"

# self - I'm referring th the current class

# print(Dog.animal_kind)
# print(Dog.bark())

# Instantiation of a class: It means making or creating an object from a class.

fido = Dog()
lassie = Dog()

print(type(fido))
print(type(lassie))
print(fido.animal_kind)
print(lassie.animal_kind)
print(fido.bark()) #it now works as we have created the object as before we only had the template.

fido.animal_kind = "Big Dog" # We can change the class from this point if we want to Dolphin for example: fido.animal_kind ="Dolphin"
# and it will now print Dolphin as we have changed the class.

# We can also overwrite the entire template by
Dog.animal_kind = "Dolphin"

print(fido.animal_kind)
print(lassie.animal_kind)

# The dogs can still access their method.

print(fido.bark())
print(lassie.bark())