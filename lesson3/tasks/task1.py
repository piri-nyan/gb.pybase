print("Division function")

def divider(number, divider):
    if divider == 0:
        raise Exception("Division by 0 is prohibited")
    else:
        return number/divider

if __name__=="__main__":
    print(divider(int(input("What to divide: ")),int(input("Divide by what: "))))