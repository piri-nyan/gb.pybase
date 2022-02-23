print("Determening loop cycle of triggered event\n")

def input_int(var_name):
    i = ''
    while type(i) is not int:
        try:
            i = int(input(f"enter int {var_name}: "))
        except Exception as e:
            pass
    return i

first_day = input_int("first day")
final_day = input_int("final day")

fitness = first_day
i=1
while fitness < final_day:
    i+=1
    fitness = fitness+(fitness/100)*10
    print(f"day {i}: {fitness}")

print(i)    