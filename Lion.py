from Animal import Animal


class Lion(Animal):

    def __init__(self):
        super().__init__()
        self.species = "Lion"

    def speak(self):
        print("The lion roars")
