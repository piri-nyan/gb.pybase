print("Converting month to season")
month = input("Enter a month number: ")
if int(month) < 1 or int(month) > 12:
    print("OwO, i guess it was 1 then")
    month = 1
else:
    month = int(month)

# list solution
winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
fall = [9, 10, 11]

year = [winter, spring, summer, fall]

for season in year:
    if month in season:
        print("Solved by lists:")
        print(f"{month} is a month in {[name for name in globals() if globals()[name] is season][0]}")

# dict solution
seasons = {'winter': [12, 1, 2],
            'spring': [3, 4, 5],
            'summer': [6, 7, 8],
            'fall': [9, 10, 11]}

for season in seasons:
    if month in seasons[season]:
        print("Solved by dictionary:")
        print(f"{month} is a month in {season}")