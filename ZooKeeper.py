from Zoo import Zoo
from Animal import Animal


class ZooKeeper:

    def __init__(self, keeper_name):
        self.keeper_name = keeper_name
        self.animal = Animal()  # Error Creating own animal object not using one from zookeeper
        self.zoo = Zoo()

    def feed_animals(self, food, animal):
        full = 5
        amount = animal.get_hunger_status() + food
        if amount > full:
            print(f"\n{animal.get_name().title()} cannot eat this much\nIt will result in overfeeding")
        else:
            animal.eat_food(food)
            print(f"\n{animal.get_name().title()} has been fed")

    def heal_animals(self, meds, animal):
        full = 10
        amount = animal.get_health_status() + meds
        if animal.get_health_status() >= 8:
            print(f"\n{animal.get_name().title()} is already healthy\nThey do not need medicating")
        elif amount > full:
            print(f"\n{animal.get_name().title()} cannot take this much medicine\nIt will result in over medicating")
        else:
            animal.take_medicine(meds)
            print(f"\n{animal.get_name().title()} has been medicated")
