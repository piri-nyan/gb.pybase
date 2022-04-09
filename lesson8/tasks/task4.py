print("Equipment")

class Warehouse():
    def __init__(self) -> None:
        pass

class Equipment():
    def __init__(self, serial, amount, cost) -> None:
        self.serial = serial
        self.amount = amount
        self.cost = cost

class Printer(Equipment):
    def __init__(self, serial, amount, cost, colored) -> None:
        super().__init__(serial, amount, cost)
        self.colored = colored

class Scanner(Equipment):
    def __init__(self, serial, amount, cost, dpi) -> None:
        super().__init__(serial, amount, cost)
        self.dpi = dpi

class Xerox(Equipment):
    def __init__(self, serial, amount, cost, ppm) -> None:
        super().__init__(serial, amount, cost)
        self.ppm = ppm


if __name__=="__main__":
    printer = Printer("123ABCP", 10, 20000, True)
    scanner = Scanner("123ABCS", 5, 10000, 3500)
    xerox = Xerox("123ABCX", 30, 30000, 15)
    print(printer, scanner, xerox)
