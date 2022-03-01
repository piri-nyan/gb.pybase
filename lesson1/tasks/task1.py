print("Just var operations\n")

a = 'string'
b = 1
c = 0.2 + 0.1 # hehe

d = str(input('Enter a string var: '))
e = ''
while type(e) is not int:
    try:
        e = int(input('Enter an int var: '))
    except Exception as ex:
        print(ex)

print(f"a: {a}\nb: {b}\nc: {c}\nd: {d}\ne: {e}")