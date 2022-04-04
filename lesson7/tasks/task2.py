print("Cloth usage calculator")

from abc import ABC, abstractmethod

class Cloth(ABC):
    def __init__(self, title, size) -> None:
        self.title = title
        self.size = size

    @abstractmethod
    def usage(self):
        pass

    def __str__(self) -> int:
        return self.usage

    def __add__(self, other):
        return self.usage+other.usage

class Coat(Cloth):
    @property
    def usage(self):
        return (self.size/6.5)+0.5

class Costume(Cloth):
    @property
    def usage(self):
        return (2*self.size)+0.3


coat = Coat("coat", 5)
costume = Costume("costume", 3)

print(coat.usage)
print(costume.usage)

print(coat+costume)