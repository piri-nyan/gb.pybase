from pprint import pprint
print("Realising goods and analytics")
goods = []
structure = ["Name", "Price", "Amount", "Unit"]
cnt = 0
sigevt = False
while True:
    good = {}
    for par in structure:
        inp = input(f"Enter goods {par} (N/n to exit): ")
        if inp.lower() != 'n':
            good[par] = inp
        else:
            sigevt = True
            break
    else:
        goods.append((cnt, good))
        cnt+=1
    if sigevt: break

pprint(goods)

stats = {}

for el in structure:
    stats[el] = []

for _, good in goods:
    for stat in structure:
        stats[stat].append(good[stat])

pprint(stats)