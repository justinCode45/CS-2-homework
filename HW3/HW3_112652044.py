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
    


seed = input("Enter a seed string: ")
print(genKey(seed))

