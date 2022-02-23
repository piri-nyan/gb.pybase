print("Counting profit of each staff member\n")

def input_int(var_name):
    i = ''
    while type(i) is not int:
        try:
            i = int(input(f"enter int {var_name}: "))
        except Exception as e:
            pass
    return i

pos = input_int("pos")
neg = input_int("neg")

if pos-neg > 0:
    rent = pos/(pos-neg)
    staff = ''

    while type(staff) is not int:
        try:
            staff = int(input("enter int staff: "))
        except Exception as e:
            pass
    
    print((pos-neg)/staff)
else:
    print(0)
