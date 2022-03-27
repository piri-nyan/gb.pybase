print("Doubles hours")

import random, re

names = ["Информатика", "Физика", "Физкультура", "Математика", "Философия", "Биология", "Химия", "История", "Обществознание", "Литература"]

with open("file", "w+", encoding="utf8") as file:
    for item in names:
        file.write(f"{item}: {' '.join([str(random.randrange(0, 100))+typo for typo in ['(л)', '(лаб)', '(пр)']])}\n")

dictionary = {}
with open("file", "r+", encoding="utf8") as file:
    for line in file.readlines():
        obj = re.match("(.*)\:\s(\d+)\(\D*\)\s(\d+)\(\D*\)\s(\d+)\(\D*\)", line)
        print(obj.groups())
        dictionary[obj.group(1)] = sum([int(x) for x in obj.groups()[1:]])

print(dictionary)