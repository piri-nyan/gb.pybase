print("Converting string to numbered lines")
inp = input("Enter a string with whitespaces:\r\n")

i = 0
for word in inp.split():
    if len(word) > 10:
        word = word[:10]
    print(f"{i} {word}")
    i+=1