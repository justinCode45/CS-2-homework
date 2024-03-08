import string

def genKey(seed: str):
    
    def rmDup(s: str):
        sP = ""
        for c in s :
            if c not in sP:
                sP += c 
        return sP
    
    def rmIn(s: str, key: str):
        sP = ""
        for c in s :
            if c not in key:
                sP += c 
        return sP
    key = string.ascii_lowercase + ' '
    seed = seed.lower() 
    seed = rmDup(seed)
    t = seed[-1]
    t = ord(t) - ord('a') if ord(t)>=ord('a') and ord(t)<=ord('z') else 26
    
    beforeLast = key[:t]
    afterLast = key[t+1:]
    
    beforeLast = rmIn(beforeLast, seed)
    afterLast = rmIn(afterLast, seed)
    
    key = seed + afterLast + beforeLast
    return key
    
def encrypt(plainText: str, key: str):
    index = lambda t : ord(t) - ord('a') if ord(t)>=ord('a') and ord(t)<=ord('z') else 26
    encryptText = ""
    for c in plainText:
        encryptText += key[index(c)]
    return encryptText

def decrypt(encryptText: str, key: str):
    char = lambda t : chr(t + ord('a')) if t != 26 else ' '
    plainText = ""
    for c in encryptText:
        plainText += char(key.index(c))
    return plainText

def main():

    seed = input("Enter a password string: ")
    print(f"Entered : {seed}")
    key = genKey(seed)
    print(f"Key : {key}")

    for _ in range(5):
        plainText = input("Enter a string to encrypt: ")
        print(f"Entered : {plainText}")
        encrptyText = encrypt(plainText, key)
        print(f"Encrypted : {encrptyText}")
        plainText = decrypt(encrptyText, key)
        print(f"Decrypted : {plainText}")

    aga = input("Continue? Y/N: ")
    if aga.lower() == "y":
        main()
    else:
        print("Goodbye")


if __name__ == "__main__" :
    main()