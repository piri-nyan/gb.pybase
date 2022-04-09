print("Only ints are allowed to the list")

class OnlyInt(Exception):
    def __init__(self):
        print("Only ints are allowed!")
        
    def __str__(self):
        return "Only ints are allowed!"


def validateVar(var):
    try:
        int(var)
    except Exception as exc:
        raise OnlyInt
    else:
        return True

def main():
    lst = []
    while True:
        inp = input("Enter element (empty to end): ")
        if inp == "":
            break
        else:
            try:
                validateVar(inp)
            except OnlyInt as exc:
                continue
            else:
                lst.append(int(inp))

    print(lst)

if __name__=="__main__":
    main()