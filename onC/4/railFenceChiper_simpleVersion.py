from wordList import *

def railEncrypt(plainText, num):
    cipherText = ['' for i in range(num)]
    for i in range(len(plainText)):
        cipherText[i % num] += plainText[i]
    return ''.join(cipherText)

def railDecrypt(cipherText, num):
    railLen = len(cipherText) // num
    plainText = ""
    for i in range(railLen):
        for j in range(num):
            plainText += cipherText[i + j * railLen]
    return plainText

plainText = "Hello World"

cipherText = railEncrypt(plainText, 3)

print(cipherText)

print(railDecrypt(cipherText, 3))

wordList = createWordList("wordlist.txt")

for i in range(1,len(cipherText)+1):
    words = railDecrypt(cipherText, i).split()
    count = 0
    for w in words:
        if w in wordList:
            count += 1
    print("Number of words in wordlist: ", count, "out of", len(words), "words. (", i, "rails)")
    