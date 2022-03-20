print("factorial with generators")

from functools import reduce

def mul(a, b):
    return a*b

def fact(n):
    for i in range(1, n+1):
        if i == 1:
            yield 1
        else:
            yield reduce(mul, range(1, i+1))

if __name__=="__main__":
    n = 4
    for el in fact(n):
        print(el)