from tier import Tier

class Gorilla(Tier):
    num_appendages = 4
    is_cold_blooded = False
    is_mammal = True

    def eat(self):
        print(f"{self.name} isst Bananen und Blätter.")

    def sleep(self):
        print(f"{self.name} rollt sich zusammen und schläft im Nest.")

    def grow(self, years):
        self.age += years
        print(f"{self.name} ist {years} Jahre älter und nun {self.age} Jahre alt.")

    def klettern(self):
        print(f"{self.name} klettert flink auf einen Baum.")