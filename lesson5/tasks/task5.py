print("Sum calc")
import random

nums = []
with open("file", "w+") as file:
    for _ in range(0, random.randrange(5, 10)):
        nums.append((str(random.randrange(0, 100))))
    file.write(" ".join(nums))

print(f"Numbers: {' '.join(nums)}")

with open("file", "r+") as file:
    print(sum([int(x) for x in file.read().split(" ")]))