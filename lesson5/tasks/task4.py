print("Convert english numbers to russian")

num2word = {"one": {"ru": "один", "num": 1},
            "two": {"ru": "два", "num": 2},
            "three": {"ru": "три", "num": 3},
            "four": {"ru": "четыре", "num": 4},
            "five": {"ru": "пять", "num": 5},
            "six": {"ru": "шесть", "num": 6},
            "seven": {"ru": "семь", "num": 7},
            "eight": {"ru": "восемь", "num": 8},
            "nine": {"ru": "девять", "num": 9},
            "zero": {"ru": "ноль", "num": 0}}


with open("file", "w+", encoding="utf8") as file:
    for key in num2word.keys():
        file.write(f"{key.capitalize()} - {num2word[key]['num']}\n")

print("Original")
with open("file", "r", encoding="utf8") as file:
    orig = file.readlines()
    print("".join(orig))

with open("file", "w+", encoding="utf8") as file:
    for line in orig:
        try:
            file.write(f"{num2word[line.split(' - ')[0].lower()]['ru'].capitalize()} - {line.split(' - ')[1]}")
        except Exception as e:
            print(e)

print("Translated")
with open("file", "r", encoding="utf8") as file:
    print(file.read())