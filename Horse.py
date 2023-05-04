from Animal import Animal


class Horse(Animal):

    def __init__(self):
        super().__init__()
        self.species = "Horse"

    def speak(self):
        print("The horse neighs")
