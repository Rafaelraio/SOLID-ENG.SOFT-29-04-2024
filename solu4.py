class Animal:
    def mover(self):
        print("O animal está se movendo.")

class Cachorro:
    def __init__(self):
        self.animal = Animal()

    def latir(self):
        print("O cachorro está latindo.")