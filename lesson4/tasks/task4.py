print("find unique numbers in list")

ex = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
fin = []


def gen():
    for i in range(len(ex)):
        if ex[i] not in ex[i+1:] and ex[i] not in ex[:i]:
            yield ex[i]

if __name__=="__main__":
    for num in gen():
        fin.append(num)
    print(fin)