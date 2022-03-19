print("First character enlargement func for a string")

import string

def pill(word) -> string:
    return word.capitalize()

def cap_all(str) -> string:
    return " ".join(map(lambda word: pill(word), str.split()))

if __name__=="__main__":
    print(cap_all("hello world"))