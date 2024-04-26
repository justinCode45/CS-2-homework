# File Name : HW8_112652044.py
# Author : Justin Chen
# Email Address : justin.sc12@nycu.edu.tw
# HW Number : 8
# Description : This program will encrypt and decrypt a message using rail fence cipher.
# Last Changed : 2024/4/26
# Dependencies : Python 3.12.2,
# Additional :

def createWordDict(filename: str) -> dict[str, bool]:
    wordDict = {}
    with open(filename, 'r') as f:
        for line in f:
            word = line.strip()
            wordDict[word] = True
    return wordDict


def rail_Encrypt(plain: str, obrit: int) -> str:
    cipher = ['' for _ in range(obrit)]
    for i in range(len(plain)):
        cipher[i % obrit] += plain[i]
    return ''.join(cipher)


def rail_Decrypt(cipher: str, obrit: int) -> str:
    plain = ""
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


def burte_force(cipher: str, wordlist: dict[str, bool]) -> tuple[int, int]:
    maxcount = -1
    argmaxOrbit = -1
    cipher = cipher.lower()
    for i in range(1, len(cipher)+1):
        words = rail_Decrypt(cipher, i)
        for c in words:
            if c.isalpha() == False:
                words = words.replace(c, ' ')
        words = words.split()
        score = 0
        for w in words:
            if wordlist.get(w, False):
                score += len(w)
        if score >= maxcount:
            maxcount = score
            argmaxOrbit = i
    return argmaxOrbit, maxcount


def main():
    wordlist = createWordDict("wordlist.txt")
    filepath = input("Please enter the file path: ")
    orbit = int(input("Please enter the number rails: "))
    with open(filepath, "r") as file:
        plain = file.read()
    cipher = rail_Encrypt(plain, orbit)
    orbit, count = burte_force(cipher, wordlist)
    print("The orbit is %d, the scores is %d" % (orbit, count))
    with open("cplain.txt", "w") as file:
        file.write(rail_Decrypt(cipher, orbit))


if __name__ == "__main__":
    main()
