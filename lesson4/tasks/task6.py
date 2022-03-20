print("itertools task")

from itertools import count, cycle

iter_fin = 10
roundabout_fin = 3

iter_res = []
cycle_res = []

def iterate(starter, fin):
    for num in count(starter):
        if num<=starter+fin:
            yield num
        else:
            break

def roundabout(lst, fin):
    i = 0
    for el in cycle(lst):
        if i <= fin*len(lst):
            yield el
            i+=1
        else:
            break

if __name__=="__main__":
    for i in iterate(3, iter_fin):
        iter_res.append(i)
    print(iter_res)

    for i in roundabout([2, 3, 5, 6], roundabout_fin):
        cycle_res.append(i)
    print(cycle_res)
