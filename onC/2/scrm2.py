def scramble2Encrypt(plainText: str):
    evenPart = ""
    oddPart = ""
    for i in range(len(plainText)):
        if i % 2 == 0:
            evenPart = evenPart + plainText[i]
        else:
            oddPart = oddPart + plainText[i]
    cipherText = oddPart + evenPart
    return cipherText

