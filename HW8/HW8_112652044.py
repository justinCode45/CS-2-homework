# File Name : HW8_112652044.py
# Author : Justin Chen
# Email Address : justin.sc12@nycu.edu.tw
# HW Number : 8
# Description : This program will encrypt and decrypt a message using rail fence cipher.
# Last Changed : 2024/4/26
# Dependencies : Python 3.12.2,
# Additional :
#   1. The score of the decrypted message is calculated by the sum of the length of the words in the message.
#   (use the number of words as the score may not be accurate)
#   2. Better interface 
import cmd
import cmd
import shlex
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
Use legacy to switch to legacy mode.
Type "help" or "?" to list commands.
            '''

    def __init__(self) -> None:
        super().__init__()
        self.wordDict: dict[str] = createWordDict("wordlist.txt")

    def do_exit(self, arg):
        '''
Usage: exit

Description:
    Exit the program.
        '''
        print("Goodbye")
        return True

    def do_encrypt(self, arg):
        '''
Usage:  encrypt <fileName> <key> [<outputFileName>]

Arguments:
    <fileName> : the name of the file to read the plain text from
    <key> : rail number
    <outputFileName> : the name of the file to write the encrypted text to      

Description:
    Encrypt a string using a key.
        '''
        arg = shlex.split(arg)
        # print(arg)
        if len(arg) < 2:
            print(ERRORPREFIX, "Invalid arguments")
            return

        plainText: str = ""

        try:
            file = open(arg.pop(0), "r")
            plainText = file.read()
            file.close()
        except:
            print(ERRORPREFIX, "File not found")
            return

        key: str = arg.pop(0)
        if not key.isnumeric():
            print(ERRORPREFIX, "Invalid arguments <keyIndex>")
            return

        encryptText = rail_Encrypt(plainText, int(key))

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

    def do_decrypt(self, arg):
        '''
Usage:  decrypt <fileName> <key> [<outputFileName>]

Arguments:
    <fileName> : the name of the file to read the encrypted text from
    <key> : rail number  
    <outputFileName> : the name of the file to write the plain text to

Description:
    Decrypt a string using a key.
        '''
        arg = shlex.split(arg)

        if len(arg) < 2:
            print("Invalid arguments")
            return

        encryptText: str = ""

        try:
            file = open(arg.pop(0), "r")
            encryptText = file.read()
            file.close()
        except:
            print(ERRORPREFIX, "File not found")
            return

        key: str = arg.pop(0)
        if not key.isnumeric():
            print(ERRORPREFIX, "Invalid arguments")
            return
        plainText = rail_Decrypt(encryptText, int(key))
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

    def do_legacy(self, arg):
        '''
Usage: legacy

Description:
    Switch to legacy mode.
        '''
        main()

    def emptyline(self):
        pass

    def do_burte_force(self, arg):
        '''
Usage: burte_force <fileName> [<outputFileName>]

Arguments:
    file <fileName> : the name of the file to read the encrypted text from
    <outputFileName> : the name of the file to write the plain text to

Description:
    Decrypt a string using brute force.

        '''
        arg = shlex.split(arg)

        if len(arg) < 1:
            print(ERRORPREFIX, "Invalid arguments")
            return

        try:
            file = open(arg.pop(0), "r")
            encryptText = file.read()
            file.close()
        except:
            print(ERRORPREFIX, "File not found")
            return

        orbit, score, wordnum = burte_force(encryptText, self.wordDict)
        print(rail_Decrypt(encryptText, orbit))
        print("The best soulution is:")
        print(f"Rail: {orbit} \n+- Score: {score} \n+- Matched Words number: {wordnum}")
        if len(arg):
            outputFileName = arg.pop(0)
            try:
                file = open(outputFileName, "w")
                file.write(rail_Decrypt(encryptText, orbit))
                file.close()
                print(f"\n{SUCCESSPREFIX}\n")
            except:
                print(ERRORPREFIX, "File not found")
                return


def createWordDict(filename: str) -> dict[str, bool]:
    wordDict = {}
    with open(filename, 'r') as f:
        for line in f:
            wordDict[line[:-1]] = True
    return wordDict


def rail_Encrypt(plain: str, obrit: int) -> str:
    cipher = ['' for _ in range(obrit)]
    for i in range(len(plain)):
        cipher[i % obrit] += plain[i]
    return ''.join(cipher)


def rail_Decrypt(cipher: str, obrit: int) -> str:
    plain = ""
    if obrit == 0:
        return cipher
    length = len(cipher) // obrit
    if len(cipher) % obrit != 0:
        length += 1
    space = obrit * length - len(cipher)
    for i in range(length-1):
        drow = 0
        for j in range(obrit):
            if i + drow < len(cipher):
                plain += cipher[i + drow]
            drow += length if j < obrit - space else length - 1
    for j in range(obrit):
        if j < obrit - space:
            plain += cipher[length-1+length * j]

    return plain


def burte_force(cipher: str, wordlist: dict[str, bool]) -> tuple[int, int, int]:
    maxscore = -1
    maxmatchWordNum = -1
    argmaxOrbit = -1
    cipher = cipher.lower()
    for i in range(len(cipher)+1):
        words = rail_Decrypt(cipher, i)
        for c in words:
            if not c.isalpha():
                words = words.replace(c, ' ')
        words = words.split()
        score = 0
        matchWordNum = 0
        for w in words:
            if wordlist.get(w, False):
                score += len(w)
                # print(w)
                matchWordNum += 1
        if score >= maxscore:
            maxscore = score
            maxmatchWordNum = matchWordNum
            argmaxOrbit = i
        print(f"Rail: {i} \n+- Score: {score} \n+- Matched Words number: {matchWordNum}")
        print("-"*50)
    return argmaxOrbit, maxscore, maxmatchWordNum


def readfile(filepath: str) -> str:
    try:
        with open(filepath, "r") as file:
            return file.read()
    except FileNotFoundError:
        print("File not found")
        exit(1)


def main():
    wordlist = createWordDict("wordlist.txt")
    # print(wordlist.get("lc",0))
    filepath = input("Please enter the file path: ")
    orbit = int(input("Please enter the number rails: "))
    with open(filepath, "r") as file:
        plain = file.read()
    cipher = rail_Encrypt(plain, orbit)
    orbit, score, wordnum = burte_force(cipher, wordlist)
    print("The best soulution is:")
    print(
        f"Rail: {orbit} \n+- Score: {score} \n+- Matched Words number: {wordnum}")
    with open("cplain.txt", "w") as file:
        file.write(rail_Decrypt(cipher, orbit))
    print("The decrypted message has been written to cplain.txt")
    print("The decrypted message is:")
    print(rail_Decrypt(cipher, orbit))


if __name__ == "__main__":
    # main()
    app().cmdloop()
