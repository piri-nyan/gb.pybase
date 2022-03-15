print("power bicycle")

def powow(x, y):
    if y >= 0:
        raise Exception("y should be negative")
    else:
        c = x
        for i in range(abs(y)-1):
            c = c * x
        return 1/c

if __name__=="__main__":
    print(powow(5, -7))