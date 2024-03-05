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

def scramble2Decrypt(cipherText):
    plainText = ""
    halfLength = len(cipherText) // 2
    oddPart = cipherText[:halfLength]
    evenPart = cipherText[halfLength:]
    for i in range(halfLength):
        plainText = plainText + evenPart[i] + oddPart[i]
    if len(oddPart) > len(evenPart):
        plainText = plainText + oddPart[-1]
    return plainText

plainText = input("Enter a string to encrypt: ")
cipherText = scramble2Encrypt(plainText)
print(f"The encrypted string is: {cipherText}")
plainText = scramble2Decrypt(cipherText)
print(f"The decrypted string is: {plainText}")

