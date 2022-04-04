print("Worker class")

import random

class Worker():
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {'wage': wage, 'bonus': bonus}

    def get_income(self):
        return self.__income

class Position(Worker):
    def get_full_name(self):
        return self.name+" "+self.surname
    
    def get_total_income(self):
        return self.get_income()['wage']+self.get_income()['bonus']

for i in range(0, 5):
    obj = Position(f"Worker{i}", f"Rekrow{i}", "vilager", random.randrange(0, 100000), random.randrange(0, 30000))
    print(obj.get_full_name(), obj.get_total_income())