# Create a Pet class with the pet attributes and methods given
class Pet:
    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
        pass

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        return self

    def noise(self):
        print("This is the pets sounds!")
        return self

# First, create a Ninja class with the ninja attributes given:

class Ninja:
    def __init__(self, first_name, last_name, treats, pet, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = Pet(pet[0], pet[1], pet[2], pet[3], pet[4]) # this line instanciates the Honey pet object when the Steven object is instantiad on line 54
        self.treats = treats
        self.pet_food =  pet_food

# these methods are inheriting the methods from the Pet class? -> i dont think so, i think its just because the imbedded methods are read first.
    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self

    def bathe(self):
        self.pet.noise()

# make an instance of a Ninja and assign them an instance of a pet to the pet attribute. 

# Honey = Pet("honey", "english_cream", "pretty", 100, 100)

Steven = Ninja("Steven", "DeTeso", "bones", ["honey", "english_cream", "pretty", 100, 100], "kibble") # the list here is instantiating the Honey object at the same time the Steven object is being instantiated. 

Steven.feed()
Steven.walk()
Steven.bathe()