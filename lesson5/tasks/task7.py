print("Firms profit counter")

from pathlib import Path
import random, json

forms = ["OOO", "OAO", "ENT", "INC"]

with open("file", "w+") as file:
    for i in range(1, 100):
        file.write(f"firm_{i} {forms[random.randrange(0, len(forms))]} {random.randrange(0, 10000)} {random.randrange(0, 10000)}\n")

profits = {}
tmp = []
average = {}

with open("file", "r+") as file:
    for line in file.readlines():
        data = line.strip().split(" ")
        profit = int(data[2]) - int(data[3])
        if profit > 0:
            print(data[0], profit)
            tmp.append(profit)
        profits[data[0]] = profit

average["average_profit"] = sum(tmp)/len(tmp)

with open("file", "w+") as file:
    json.dump([profits, average], file, indent=4)