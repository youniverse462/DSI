from tier import Tier

class Tiger(Tier):
    num_appendages = 4
    is_cold_blooded = False
    is_mammal = True

    def eat(self):
        print(f"{self.name} frisst Fleisch wie ein echter Tiger!")

    def sleep(self):
        print(f"{self.name} schläft in der Sonne wie ein fauler Tiger.")

    def grow(self, years):
        self.age += years
        print(f"{self.name} ist ein größerer Tiger geworden: {self.age} Jahre alt.")

    def schleichen(self):
        print(f"{self.name} schleicht lautlos durch das Gehege.")