class Animal:
    def mover(self):
        print("O animal está se movendo.")

class Fazenda:
    def __init__(self):
        self.animal = Animal()

    def abrir(self):
        print("A fazenda está abrindo.")