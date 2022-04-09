print("Operations on complex numbers")

class ComplexNum():
    def __init__(self, Main, Part) -> None:
        self.Main = Main
        self.Part = Part

    def __add__(self, other):
        return ComplexNum((self.Main + other.Main), (self.Part + other.Part))

    def __mul__(self, other):
        return ComplexNum((self.Main*other.Main)-(self.Part*other.Part), (self.Part*other.Main)+(self.Main*other.Part))

    def __str__(self) -> str:
        return f"{self.Main}, {self.Part}"

if __name__=="__main__":
    a = ComplexNum(5, 3)
    b = ComplexNum(6, 2)

    print(a+b)
    print(a*b)