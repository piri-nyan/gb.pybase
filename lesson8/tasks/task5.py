print("Warehouse operations")

from task4 import Warehouse, Printer, Scanner, Xerox

class Warehouse(Warehouse):
    def __init__(self) -> None:
        super().__init__()
        self.eq = {}

    def ImportEq(self, equ):
        self.eq[equ.serial] = equ
        print(self.eq)

    def ExportEq(self, equ):
        del self.eq[equ.serial]
        print(self.eq)



if __name__=="__main__":
    warehouse = Warehouse()
    printer = Printer("123ABCP", 10, 20000, True)
    scanner = Scanner("123ABCS", 5, 10000, 3500)
    xerox = Xerox("123ABCX", 30, 30000, 15)
    warehouse.ImportEq(printer)
    warehouse.ImportEq(scanner)
    warehouse.ImportEq(xerox)
    warehouse.ExportEq(printer)
    warehouse.ExportEq(scanner)
    warehouse.ExportEq(xerox)