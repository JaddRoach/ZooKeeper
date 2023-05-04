from Animal import Animal


class Tiger(Animal):

    def __init__(self):
        super().__init__()
        self.species = "Tiger"

    def speak(self):
        print("The tiger roars")
