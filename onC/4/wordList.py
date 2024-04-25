def createWordList(filename):
    wordList = []
    with open(filename, 'r') as f:
        for line in f:
            word = line.strip()
            wordList.append(word)
    return wordList

if __name__ == "__main__":
    createWordList("wordlist.txt")