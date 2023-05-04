from Animal import Animal


class Elephant(Animal):

    def __init__(self):
        super().__init__()
        self.species = "Elephant"

    def speak(self):
        print("The elephant trumpets")

