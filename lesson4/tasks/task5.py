print("finding even numbers between 100 and 1000")

from functools import reduce

even = []

def mul(a, b):
    return a*b

def gen():
    for i in range(100, 1001):
        if i % 2 == 0:
            yield i

if __name__=="__main__":
    for num in gen():
        even.append(num)
    print(reduce(mul, even))
    