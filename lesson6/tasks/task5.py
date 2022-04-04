print("Stationery classes with individual draw's")

from abc import ABC, abstractmethod

class Stationery(ABC):
    def __init__(self, title) -> None:
        self.title = title

    @abstractmethod
    def draw(self):
        pass

class Pen(Stationery):
    def draw(self):
        return f"drawing blue line with {self.title}"

class Pencil(Stationery):
    def draw(self):
        return f"drawing almost invisible line with {self.title}"

class Handle(Stationery):
    def draw(self):
        return f"drawing wide line line with {self.title}"

pen = Pen("PEN")
pencil = Pencil("PENCIL")
handle = Handle("HANDLE")

print(pen.draw())
print(pencil.draw())
print(handle.draw())