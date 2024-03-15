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
import cmd
import shlex


class app(cmd.Cmd):

    prompt = "\033[93m>> \033[0m"
    intro = '''
This program encrypts and decrypts strings using a keyword.
Type "help" or "?" to list commands.
            '''
    keyList: list[str] = []
    encryptedList: list[str] = []

    def __init__(self) -> None:
        super().__init__()

    def do_exit(self, arg):
        '''
Usage: exit

Description:
    Exit the program.
        '''
        print("Goodbye")
        return True

    def do_genkey(self, arg):
        '''

Usage: genkey <string>

Arguments:
    <string> : the password to generate the key

Description:
    Generate a key from the password.
    Use the "keylist" command to list all keys.

        '''
        s = genKey(arg)
        self.keyList.append(s)
        print(f"You Entered : {arg}")
        print(f"  Key : {s}")
        print(f"Index : {len(self.keyList)}")
        print()

    def do_loadkey(self, arg):
        '''
Usage: loadkey <fileName>

Arguments:
    <fileName> : the name of the file to read the key from

Description:
    Load a key from a file.
        '''
        try:
            file = open(arg, "r")
            s = file.read()
            file.close()
            self.keyList.append(s)
            print()
            print(f"  Key : {s}")
            print(f"Index : {len(self.keyList)}")
            print()
        except:
            print("File not found")

    def do_encrypt(self, arg):
        '''
Usage:  encrypt file <fileName> <keyIndex> [<outputFileName>]
        encrypt str <string> <keyIndex> [<outputFileName>]

Arguments:
    file <fileName> : the name of the file to read the plain text from
    str <string> : the plain text to encrypt
    <keyIndex> : the index of the key to use
    <outputFileName> : the name of the file to write the encrypted text to      

Description:
    Encrypt a string using a key.
    Use the "keylist" command to list all keys.
        '''
        arg = shlex.split(arg)
        # print(arg)
        if len(arg) < 3:
            print("Invalid arguments")
            return

        plainText: str = ""

        match arg.pop(0):
            case "file":
                try:
                    file = open(arg.pop(0), "r")
                    plainText = file.read()
                    file.close()
                except:
                    print("File not found")
                    return
            case "str":
                plainText = arg.pop(0)
            case _:
                print("Invalid arguments")
                return

        key: str = arg.pop(0)
        if not key.isnumeric():
            print("Invalid arguments <keyIndex>")
            return
        key = int(key) - 1
        if key < 0 or key >= len(self.keyList):
            print("Invalid key index")
            return
        key = self.keyList[key]

        encryptText = encrypt(plainText, key)

        if len(arg):
            outputFileName = arg.pop(0)
            try:
                file = open(outputFileName, "w")
                file.write(encryptText)
                file.close()
                print("\nSuccess!\n")
            except:
                print("File not found")
                return
        else:
            print(encryptText)
            self.encryptedList.append(encryptText)
            print(f"Encrypted text added to list at index {len(self.encryptedList)}")

    def do_decrypt(self, arg):
        '''
Usage:  decrypt file <fileName> <keyIndex> [<outputFileName>]
        decrypt str <string> <keyIndex> [<outputFileName>]
        decrypt list <listIndex> <keyIndex> [<outputFileName>]

Arguments:
    file <fileName> : the name of the file to read the encrypted text from
    str <string> : the encrypted text to decrypt
    list <listIndex> : the index of the encrypted text to decrypt
    <keyIndex> : the index of the key to use
    <outputFileName> : the name of the file to write the plain text to

Description:
    Decrypt a string using a key.
    Use the "keylist" command to list all keys.
        '''
        arg = shlex.split(arg)

        if len(arg) < 3:
            print("Invalid arguments")
            return

        encryptText: str = ""

        match arg.pop(0):
            case "file":
                try:
                    file = open(arg.pop(0), "r")
                    encryptText = file.read()
                    file.close()
                except:
                    print("File not found")
                    return
            case "str":
                encryptText = arg.pop(0)
            case "list":
                index = arg.pop(0)
                if not index.isnumeric():
                    print("Invalid arguments")
                    return
                index = int(index) - 1
                if index < 0 or index >= len(self.encryptedList):
                    print("Invalid list index")
                    return
                encryptText = self.encryptedList[index]
                self.encryptedList.pop(index)
            case _:
                print("Invalid arguments")
                return

        key: str = arg.pop(0)
        if not key.isnumeric():
            print("Invalid arguments")
            return
        key = int(key) - 1
        if key < 0 or key >= len(self.keyList):
            print("Invalid key index")
            return
        key = self.keyList[key]

        plainText = decrypt(encryptText, key)

        if len(arg):
            outputFileName = arg.pop(0)
            try:
                file = open(outputFileName, "w")
                file.write(plainText)
                file.close()
            except:
                print("File not found")
                return
        else:
            print(plainText)

    def do_keylist(self, arg):
        '''
Usage: keylist

Description:
    List all keys.
        '''
        print()
        print(f"{"Key List":-^32}")
        for i in range(len(self.keyList)):
            print(f"{i+1:2} : {self.keyList[i]}")
        print()

    def do_defualtMode(self, arg):
        '''
Usage: defualtMode

Description:
    Switch to defualt mode.
        '''
        main()

    def do_etextlist(self, arg):
        '''
Usage: etextlist

Description:
    List all encrypted text.
        
        '''
        print()
        print(f"{"Encrypted Text List":-^32}")
        for i in range(len(self.encryptedList)):
            print(f"{i+1:2} : {self.encryptedList[i]}")
        print()

    def emptyline(self):
        pass

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

    def toindex(t):
        if ord(t) >= ord('a') and ord(t) <= ord('z'):
            return ord(t) - ord('a')
        else:
            return 26

    encryptText = ""
    for c in plainText:
        c = c.lower()
        encryptText += key[toindex(c)]
    return encryptText


def decrypt(encryptText: str, key: str) -> str:

    def tochar(t):
        return chr(t + ord('a')) if t != 26 else ' '

    plainText = ""
    for c in encryptText:
        c = c.lower()
        plainText += tochar(key.index(c))
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
    app().cmdloop()
