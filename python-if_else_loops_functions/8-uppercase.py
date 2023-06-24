#!/usr/bin/python3#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if letter >= 'a' and letter <= 'z':
            let = chr(ord(letter) - 32)
        else:
            let = letter
        print(f"{let}", end="")
    print("")
