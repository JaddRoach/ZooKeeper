import random


class Animal:
    def __init__(self):
        self.species = ""
        self.name = ""
        self.hunger_status = random.randint(1, 5)
        self.health_status = random.randint(1, 10)

    def get_species(self):
        return self.species

    def set_species(self, species):
        self.species = species

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_hunger_status(self):
        return self.hunger_status

    def set_hunger_status(self, hunger):
        self.hunger_status = hunger

    def get_health_status(self):
        return self.health_status

    def set_health_status(self, health):
        self.health_status = health

    def eat_food(self, food):
        self.hunger_status += food

    def take_medicine(self, meds):
        self.health_status += meds

    def speak(self):
        print("Make Noise")



