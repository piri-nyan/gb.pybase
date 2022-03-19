print("neverending sum")

import os

summary = 0
while True:
    nums = input("Enter numbers divided by whitespace: ")
    if "!" in nums and len(nums)==1:
        break
    elif "!" in nums:
        nums = nums.split("!")[0]
        nums = nums.split()
        summary += sum(list(map(lambda x: int(x), nums)))
        print(" "*os.get_terminal_size().columns+"\r"+str(summary))
        break
    else:
        nums = nums.split()
        summary += sum(list(map(lambda x: int(x), nums)))
        print(" "*os.get_terminal_size().columns+"\r"+str(summary)+"\r", end="\033[F"+" "*os.get_terminal_size().columns+"\r")