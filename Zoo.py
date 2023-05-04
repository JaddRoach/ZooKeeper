class Zoo:

    def __init__(self):
        self.cages = []

    def add_animals(self, animal):
        self.cages.append(animal)

    def show_animals(self):
        if self.cages:
            for cage in self.cages:
                print(f"\nName : {cage.get_name().title()}")
                print(f"Species : {cage.get_species().title()}")
                print(f"Hunger Status : {cage.get_hunger_status()}")
                print(f"Health Status : {cage.get_health_status()}")
        else:
            print("The cages are empty")

    def show_animal_name(self):
        if self.cages:
            for cage in self.cages:
                print(f"\nName : {cage.get_name().title()}")

    def get_animal(self, location):
        animal = self.cages[location]
        return animal
