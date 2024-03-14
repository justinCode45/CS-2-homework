# File Name : HW3_112652044.py
# Author : Justin Chen
# Email Address : justin.sc12@nycu.edu.tw
# HW Number : 3
# Description :
# Last Changed : 2024/3/14
# Dependencies : Python 3.12.2 ,matplotlib, numpy
# Additional :
#   1. Check user input is safe


import string

# def colorStr()

def genKey(seed: str) -> str:

    def rmDup(s: str):
        sP: string = ""
        for c in s:
            if c not in sP:
                sP += c
        return sP

    def rmIn(s: str, key: str):
        sP: string = ""
        for c in s:
            if c not in key:
                sP += c
        return sP

    key = string.ascii_lowercase + ' '
    seed = seed.lower()
    seed = rmDup(seed)
    t = seed[-1]
    t = ord(t) - ord('a') if ord(t) >= ord('a') and ord(t) <= ord('z') else 26

    beforeLast = key[:t]
    afterLast = key[t+1:]

    beforeLast = rmIn(beforeLast, seed)
    afterLast = rmIn(afterLast, seed)

    key = seed + afterLast + beforeLast
    return key


def encrypt(plainText: str, key: str) -> str:

    def index(t):
        if ord(t) >= ord('a') and ord(t) <= ord('z'):
            return ord(t) - ord('a')
        else:
            return 26

    encryptText = ""
    for c in plainText:
        encryptText += key[index(c)]
    return encryptText


def decrypt(encryptText: str, key: str) -> str:

    def char(t):
        return chr(t + ord('a')) if t != 26 else ' '

    plainText = ""
    for c in encryptText:
        plainText += char(key.index(c))
    return plainText


def checkInput(input: str) -> str:
    safeInput: str = ""
    for i in input:
        if i in string.ascii_letters or i == ' ':
            safeInput += i
    return safeInput


def main():

    print("This program encrypts and decrypts strings using a keyword")
    seed = input("Enter a password string: ")
    print(f"Entered : {seed}")
    seed = checkInput(seed)
    key = genKey(seed)
    print(f"Key : {key}")

    for _ in range(5):
        plainText = input("Enter a string to encrypt: ")
        print(f"Entered : {plainText}")
        encrptyText = encrypt(plainText, key)
        print(f"Encrypted : {encrptyText}")
        plainText = decrypt(encrptyText, key)
        print(f"Decrypted : {plainText}")

    again = input("Continue? Y/N: ")
    if again.lower() == "y":
        main()
    else:
        print("Goodbye")


if __name__ == "__main__":
    main()
