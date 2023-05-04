from Animal import Animal


class Peacock(Animal):

    def __init__(self):
        super().__init__()
        self.species = "Peacock"

    def speak(self):
        print("The peacock pecks")
