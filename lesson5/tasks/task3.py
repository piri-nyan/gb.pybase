print("Mean wage calc")

import random

surnames = ['Смирнов',
            'Иванов',
            'Кузнецов',
            'Соколов',
            'Попов',
            'Лебедев',
            'Козлов',
            'Новиков',
            'Морозов',
            'Петров']

tmp = {} # minimizing file opennings

file = open("file", "w+", encoding="utf8")

for surname in surnames:
    wage = random.randrange(10000, 30000)
    tmp[surname] = wage
    file.write(f"{surname} {wage}\n")

file.close()

for entity in tmp:
    if tmp[entity] < 20000:
        print(entity)