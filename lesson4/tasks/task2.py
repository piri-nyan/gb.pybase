print("list numbers bigger than previous")

ex = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
fin = []

def gen():
    for i in range(1, len(ex)):
        if ex[i] > ex[i-1]:
            yield(ex[i])

if __name__=="__main__":
    for number in gen():
        fin.append(number)
    print(fin)