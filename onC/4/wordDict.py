def createWordDict(filename):
    wordDict = {}
    with open(filename, 'r') as f:
        for line in f:
            word = line.strip()
            wordDict[word] = True
    return wordDict

if __name__ == "__main__" : 
    createWordDict("wordlist.txt")