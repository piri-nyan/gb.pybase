print("Evaluating profits\n")

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
    print("profit")
elif pos-neg < 0:
    print("loss")
else:
    print("zero")