print("Custom exception")

class ZeroDiv(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __str__(self) -> str:
        return "Division by zero"


def ZeroDivRaiser(a, b):
    if b == 0:
        raise ZeroDiv
    else:
        c = a/b
        return c


try:
    ZeroDivRaiser(int(input("Enter dividend: ")), int(input("Enter divisor: ")))
except ZeroDiv as err:
    print(err)