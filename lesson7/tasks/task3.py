print("Spores")

class Cell():
    def __init__(self, cores) -> None:
        self.cores = int(cores)

    def __str__(self) -> str:
        return str(self.cores)

    def __add__(self, other):
        return Cell(self.cores+other.cores)

    def __sub__(self, other):
        if self.cores-other.cores<0:
            print("Trying to substitue a bigger cell")
            return Cell(self.cores)
        else:
            return Cell(self.cores-other.cores)

    def __mul__(self, other):
        return Cell(self.cores*other.cores)

    def __truediv__(self, other):
        return Cell(self.cores//other.cores)

    def make_order(self, per_row):
        tmp = self.cores
        for _ in range(0, self.cores//per_row+1):
            if tmp>=per_row:
                print("*"*per_row)
                tmp-=per_row
            else:
                print("*"*tmp)
                tmp-=tmp


cell1 = Cell(6)
cell2 = Cell(2)

print(cell1+cell2+cell1)
print(cell1+cell2+cell1-cell2)
print(cell2-(cell1+cell2+cell1))
print(cell1/cell2)
print("MAKE ORDER")
print((cell1+cell2+cell1).make_order(4))