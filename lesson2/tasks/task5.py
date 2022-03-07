print("Raiting realisation")
raiting = []

while True:
    inp = input("Enter a new value (N/n to exit): ")
    if inp.lower() == 'n':
        break
    else:
        raiting.append(int(inp))
    print(sorted(raiting, reverse=True))

print(f"Final raiting is {sorted(raiting, reverse=True)}")