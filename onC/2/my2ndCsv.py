with open("query.csv","r",encoding="utf8") as inFile:
    with open("mag2.txt","w") as outFile:
        allData = inFile.readlines()
        theTitle = allData[0].split(',')
        # print(theTitle)
        col = 0 
        while theTitle[col] != 'mag':
            col = col+1
        print("The magnitude is in col",col)
        for aLine in allData[1:] :
            c = aLine.split(',')
            print(c)
            outFile.write(c[col] + '\n')
