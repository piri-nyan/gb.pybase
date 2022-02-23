print("Finding biggest digit in number\n")

n = ''
while type(n) is not int:
    try:
        n = int(input("enter int n: "))
    except Exception as e:
        pass
i = 0
max = 0
while i < len(str(n)):
    if int(str(n)[i]) > max:
        max = int(str(n)[i])
    else:
        pass
    i+=1

print(max)