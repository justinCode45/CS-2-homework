# File Name : HW3_112652044.py
# Author : Justin Chen
# Email Address : justin.sc12@nycu.edu.tw
# HW Number : 3
# Description :
# Last Changed : 2024/3/14
# Dependencies : Python 3.12.2 ,matplotlib, numpy
# Additional :
#   1. Check user input is safe
#   2. Can save and load key to file
#   3. Can encrypt and decrypt file

import string
import cmd
import shlex
import secrets
import random
import time
import math
from enum import Enum


class FgColor(Enum):
    BLACK = "30"
    RED = "31"
    GREEN = "32"
    YELLOW = "33"
    BLUE = "34"
    MAGENTA = "35"
    CYAN = "36"
    WHITE = "37"


def color(s: str, c: FgColor) -> str:
    return f"\033[{c.value}m{s}\033[0m"


ERRORPREFIX: str = "[" + color("Error", FgColor.RED) + "]"
SUCCESSPREFIX: str = "[" + color("Success", FgColor.GREEN) + "]"


class app(cmd.Cmd):

    prompt = "\033[93m>> \033[0m"
    intro = '''
This program encrypts and decrypts strings using a keyword.
If want to exit, type "exit".
If want to switch to legacy mode, type "legacy".
Type "help" or "?" to list commands.
            '''
    keyList: list[str] = []
    encryptedList: list[str] = []

    def __init__(self) -> None:
        super().__init__()
        self.mcmc = MCMC()

    def do_savekey(self, arg):
        '''
Usage: savekey <keyIndex> <fileName>

Arguments:
    <keyIndex> : the index of the key to save
    <fileName> : the name of the file to save the key to

Description:
    Save a key to a file.
        '''
        arg = shlex.split(arg)
        if len(arg) != 2:
            print(ERRORPREFIX, "Invalid arguments")
            return
        keyIndex = arg.pop(0)
        if not keyIndex.isnumeric():
            print(ERRORPREFIX, "Invalid arguments")
            return
        keyIndex = int(keyIndex) - 1
        if keyIndex < 0 or keyIndex >= len(self.keyList):
            print(ERRORPREFIX, "Invalid key index")
            return
        key = self.keyList[keyIndex]
        fileName = arg.pop(0)
        try:
            file = open(fileName, "w")
            file.write(key)
            file.close()
            print(f"\n{SUCCESSPREFIX}\n")
        except:
            print(ERRORPREFIX, "File not found")

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
        print()
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
            print(ERRORPREFIX, "File not found")

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
            print(ERRORPREFIX, "Invalid arguments")
            return

        plainText: str = ""

        match arg.pop(0):
            case "file":
                try:
                    file = open(arg.pop(0), "r")
                    plainText = file.read()
                    file.close()
                except:
                    print(ERRORPREFIX, "File not found")
                    return
            case "str":
                plainText = arg.pop(0)
            case _:
                print(ERRORPREFIX, "Invalid arguments")
                return

        key: str = arg.pop(0)
        if not key.isnumeric():
            print(ERRORPREFIX, "Invalid arguments <keyIndex>")
            return
        key = int(key) - 1
        if key < 0 or key >= len(self.keyList):
            print(ERRORPREFIX, "Invalid key index")
            return
        key = self.keyList[key]

        encryptText = encrypt(plainText, key)

        if len(arg):
            outputFileName = arg.pop(0)
            try:
                file = open(outputFileName, "w")
                file.write(encryptText)
                file.close()
                print(f"\n{SUCCESSPREFIX}\n")
            except:
                print(ERRORPREFIX, "File not found")
                return
        else:
            print(encryptText)
            self.encryptedList.append(encryptText)
            l = len(self.encryptedList)
            print(f"Encrypted text added to list at index {l}")

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
                    print(ERRORPREFIX, "File not found")
                    return
            case "str":
                encryptText = arg.pop(0)
            case "list":
                index = arg.pop(0)
                if not index.isnumeric():
                    print(ERRORPREFIX, "Invalid arguments")
                    return
                index = int(index) - 1
                if index < 0 or index >= len(self.encryptedList):
                    print(ERRORPREFIX, "Invalid list index")
                    return
                encryptText = self.encryptedList[index]
                self.encryptedList.pop(index)
            case _:
                print(ERRORPREFIX, "Invalid arguments")
                return

        key: str = arg.pop(0)
        if not key.isnumeric():
            print(ERRORPREFIX, "Invalid arguments")
            return
        key = int(key) - 1
        if key < 0 or key >= len(self.keyList):
            print(ERRORPREFIX, "Invalid key index")
            return
        key = self.keyList[key]

        plainText = decrypt(encryptText, key)

        if len(arg):
            outputFileName = arg.pop(0)
            try:
                file = open(outputFileName, "w")
                file.write(plainText)
                file.close()
                print(f"\n{SUCCESSPREFIX}\n")
            except:
                print(ERRORPREFIX, "File not found")
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

    def do_legacy(self, arg):
        '''
Usage: legacy

Description:
    Switch to legacy mode.
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

    def do_MCMC(self, arg):
        '''
Usage: MCMC <fileName> <iteration> <outputFileName>

Arguments:
    <fileName> : the name of the file to read the encrypted text from
    <iteration> : the number of iteration to run
    <outputFileName> : the name of the file to write the plain text to

Description:
    Decrypt a string using a Markov Chain Monte Carlo.
    the reference file and  encrypted text file should be SAFE.
    ONLY HAVE LOWERCASE LETTERS AND SPACE.
        '''
        arg = shlex.split(arg)
        if len(arg) != 3:
            print(ERRORPREFIX, "Invalid arguments")
            return
        infile = arg.pop(0)
        iteration = arg.pop(0)
        outfile = arg.pop(0)
        if not iteration.isnumeric():
            print(ERRORPREFIX, "Invalid arguments")
            return
        iteration = int(iteration)
        self.mcmc.run(infile, iteration, outfile)


class MCMC:

    uniDict: dict[str, str] = {}
    biDict: dict[str, str] = {}

    def __init__(self) -> None:
        self.p = 1

    def buildDict(self, refpath: str, freqTargetList: list[str]) -> None:
        with open(refpath, "r") as file:
            ref = file.read()
        self.uniDict = self.freqDict(ref, string.ascii_lowercase + ' ')
        self.biDict = self.freqDict(ref, freqTargetList)

    def freqDict(self, refpath: str, freqTargetList: list[str]) -> dict:

        with open(refpath, "r") as file:
            ref = file.read()
        ref.lower()
        freq = {}
        for key in freqTargetList:
            freq[key] = ref.count(key)
        return freq

    def nextKey(self, key: str) -> str:
        i, j = random.sample(range(0, 26), 2)
        key = list(key)
        key[i], key[j] = key[j], key[i]
        return ''.join(key)

    def score(self, textDict: dict[str, str], refDict: dict[str, str]) -> int:
        lscore: int = 0
        for k in textDict:
            lscore += textDict[k]*math.log2(refDict[k])
        return lscore

    def attack(self, otext: str, key: str, frqList) -> str:
        newkey = self.nextKey(key)
        newtext = decrypt(otext, newkey)
        currenttext = decrypt(otext, key)
        currentDict = self.freqDict(currenttext, frqList)
        newDict = self.freqDict(newtext, frqList)

        newScore = self.score(newDict, self.uniDict)
        currentScore = self.score(currentDict, self.uniDict)

        scorep: float = newScore/currentScore
        scorep = math.pow(scorep, self.p)
        u = secrets.randbelow(1)

        if u < scorep:
            key = newkey

        return key

    def run(self, infile: str, iteration: int, outfile: str) -> None:
        bifreqKeyList = []
        self.buildDict("ref.txt", bifreqKeyList)

        with open(infile, "r") as file:
            otext = file.read()
        otext = otext.lower()

        startkey = "dkflstuvwxyz abceghijmnopqr"
        for _ in range(10):
            startkey = self.attack(otext, startkey, string.ascii_lowercase+' ')
        rtemp = random.randint(0, len(otext) - 10000)
        otext = otext[rtemp:2000]

        keyList = []
        keyNow = startkey
        for i in range(iteration):
            keyNow = self.attack(otext, keyNow, bifreqKeyList)
            if keyNow not in keyList:
                keyList.append(keyNow)

        with open(infile, "r") as file:
            otext = file.read()
        otext = otext.lower()

        keyscore = []
        for key in keyList:
            text = decrypt(otext, key)
            textDict = self.freqDict(text, bifreqKeyList)
            keyscore.append((key, self.score(textDict, self.biDict)))

        maxScoreKey = max(keyscore, key=lambda x: x[1])
        key = maxScoreKey[0]

        with open(outfile, "w") as file:
            file.write(decrypt(otext, key))
        print(f"\n{SUCCESSPREFIX}\n")
        print(f"Key : {key}")


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
    # main()
    random.seed(time.time())
    app().cmdloop()
