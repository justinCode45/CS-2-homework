def substitutionEncrypt(plainText: str, key: str):
    from string import ascii_lowercase
    alphabet = ascii_lowercase + ' '
    cipherText = ''
    plainText = plainText.lower()
    for ch in plainText:
        idx = alphabet.find(ch)
        cipherText = cipherText + key[idx]
    return cipherText

plainText = input("Enter the message to encrypt: ")
key1 = "zyxwvutsrqponmlkjihgfedcba "
cipherText = substitutionEncrypt(plainText, key1)
print(f"The encrypted message is: {cipherText}")

key2 = "abcdefghijkl mnopqrstuvwxyz"
cipherText = substitutionEncrypt(plainText, key2)
print(f"The encrypted message is: {cipherText}")
