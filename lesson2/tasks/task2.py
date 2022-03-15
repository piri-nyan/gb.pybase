from numpy import NaN


print("Interchanging neighbours")
arr = []

while True:
    inp = input("Enter a value (N/n to exit): ")
    if inp.lower() != 'n':
        arr.append(inp)
    else: break

for i in range(0, len(arr), 2):
    try:
        tmp = arr[i+1]
        arr[i+1] = arr[i]
        arr[i] = tmp
    except:
        pass

print(arr)