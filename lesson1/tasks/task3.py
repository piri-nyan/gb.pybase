print("Finding n+nn+nnn\n")

n = ''
while type(n) is not int:
    try:
        n = int(input("enter int n: "))
    except Exception as e:
        pass

print(n+int(str(n)*2)+int(str(n)*3))