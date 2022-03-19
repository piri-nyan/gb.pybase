print("First character enlargement func")

import string

def pill(word) -> string:
    return word.capitalize()

if __name__=="__main__":
    print(pill("hello"))