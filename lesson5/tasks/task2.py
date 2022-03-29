print("Count word and chars")

with open("file", "r") as f:
    txt = f.read()

characters = 0
words = 1 # because first or last word isnt whitespaces
for char in txt:
    if char is " ":
        words+=1
    else:
        characters+=1

print(characters, words)