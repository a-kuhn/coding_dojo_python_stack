# Imagine a game where you can create a zoo and start raising different types of animals. Say that for each zoo you create can have several different animals. 
# 
# **1** ~~DONE~~ Start by creating an Animal class, and then 
# **2** ~~DONE~~ at least 3 specific animal classes that inherit from Animal. (Maybe lions and tigers and bears, oh my!) 
# **3** ~~DONE~~ Each animal should at least have a name, an age, a health level, and happiness level. 
# **4** ~~DONE~~ The Animal class should have a display_info method that shows the animal's name, health, and happiness. 
# **5** ~~DONE~~ It should also have a feed method that increases health and happiness by 10.

# **6** ~~DONE~~ || Marsupial: weight || In at least one of the Animal child classes you've created, add at least one unique attribute. 
# **7** ~~DONE~~ Give each animal different default levels of health and happiness. 
# **8** ~~DONE~~ The animals should also respond to the feed method with varying levels of changes to health and happiness.
# **8b** ~~DONE~~ || Bird: playtime() || Give one animal a unique method.

# **9** ~~DONE~~ Once you've tested out your different animals and feel more comfortable with inheritance, create a Zoo class to help manage all your animals.

class Zoo:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.animals = []
    
    def display_zoo_info(self):
        animal_count = len(self.animals)
        print(f"Welcome to the {self.name} zoo! We are located in {self.location} and currently house {animal_count} animals.")
    
    def display_animals_info(self):
        for animal in self.animals:
            animal.displayInfo()
        return self

    def add_animal(self, animal_name, age, health, happiness, animal_type):
        self.animals.append(animal_type(animal_name, age, health, happiness))
        return self



class Animal:
    def __init__(self, animal_name, age, health, happiness):
        self.animal_name = animal_name
        self.age = age
        self.health = health
        self.happiness = happiness

    def displayInfo(self):
        print(f"{self.animal_name} is {self.age} years old, has a health level of {self.health} and a happiness level of {self.happiness}.")
        return self

    def feed(self):
        self.health += 10
        self.happiness += 10
        return self
    
class Marsupial(Animal):
    def __init__(self, animal_name, age, weight, health=6, happiness=4):
        super().__init__(animal_name, age, health, happiness)
        self.weight = weight

    def feed(self):
        self.health += 6
        self.happiness += 10
        return self

class Reptile(Animal):
    def __init__(self, animal_name, age, health=7, happiness=10):
        super().__init__(animal_name, age, health, happiness)
    
    def feed(self):
        self.health += 10
        self.happiness += 7
        return self


class Bird(Animal):
    def __init__(self, animal_name, age, health=8, happiness=7):
        super().__init__(animal_name, age, health, happiness)

    def feed(self):
        self.health += 9
        self.happiness += 5
        return self
    
    def playtime(self, lengthInMinutes):
        self.happiness += 0.1 * lengthInMinutes
        return self

# make animals
trashy = Marsupial("trashy", 3, 6.8)
mr_scales = Reptile("mr_scales", 7)
birb = Bird("birb", 2)

#test feed()
trashy.feed()
mr_scales.feed()
birb.feed()

#test displayInfo()
trashy.displayInfo()
mr_scales.displayInfo()
birb.displayInfo()

#test playtime()
birb.playtime(20)

#make a zoo
animal_kingdom = Zoo("animal_kingdom", "Santa Ana, CA")

#add animals
animal_kingdom.add_animal("stella", 2, 5, 5, Marsupial)
animal_kingdom.add_animal("flit", 8, 7, 9, Bird)

#add already-existing animals to a zoo
animal_kingdom.animals.append(trashy)
animal_kingdom.animals.append(mr_scales)
animal_kingdom.animals.append(birb)
#test print animals dict -- also tests aninmal.displayInfo()
animal_kingdom.display_animals_info()

#test zoo.display_zoo_info()
animal_kingdom.display_zoo_info()
