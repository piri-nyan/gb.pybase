print("Warehouse import validation")

from task5 import Warehouse, Printer, Scanner, Xerox

class Warehouse(Warehouse):
    def __init__(self) -> None:
        super().__init__()

    def ImportEq(self, equ):
        if self.ValidateEq(equ):
            return super().ImportEq(equ)
        else:
            print("Import validation failed")

    def ValidateEq(self, equ):
        try:
            int(equ.amount)
        except Exception as exc:
            print(exc)
            return False
        else:
            return True


if __name__=="__main__":
    warehouse = Warehouse()
    printer = Printer("123ABCP", 10, 20000, True)
    scanner = Scanner("123ABCS", "five", 10000, 3500)
    xerox = Xerox("123ABCX", "30", 30000, 15)
    warehouse.ImportEq(printer)
    warehouse.ImportEq(scanner)
    warehouse.ImportEq(xerox)