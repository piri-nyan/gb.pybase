print("Converting seconds to readable time format\n")

time = ''
while type(time) is not int:
    try:
        time = int(input("time in secs: "))
    except Exception as e:
        pass

hours = time//(60*60)
time -= hours*60*60
minutes = time//60
seconds = time%60

print(f"{hours}:{minutes}:{seconds}")