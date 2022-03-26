print("Creating a file and write inputs")

with open("file", "w+") as f:
    while True:
        inp = input("Write: ")
        if not inp:
            break
        else:
            f.write(inp)

