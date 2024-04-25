with open("wordlist.txt","r") as wordFile:
    for i in range(10):
        word = wordFile.readline().strip()
        print(word)