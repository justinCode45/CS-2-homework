def removeChar(s, c):
    return s[:c] + s[c+1:]

def keyGen():
    import random
    from string import ascii_lowercase
    alphabet = ascii_lowercase + ' '
    key = ""
    for i in range(len(alphabet)-1,-1,-1):
        idx = random.randint(0,i)
        key = key + alphabet[idx]
        alphabet = removeChar(alphabet, idx)
    return key


print(keyGen())