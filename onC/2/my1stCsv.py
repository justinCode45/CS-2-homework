import csv

with open("query.csv","r",encoding="utf8") as inFile:
    with open("magl.txt","w") as outFile:
        theReader = csv.reader(inFile)
        theTitle = next(theReader)
        print(theTitle)
        col = 0
        while theTitle[col] != 'mag':
            col += 1
        print("The magntiude in col",col)
        for aLine in theReader:
            print(aLine)
            outFile.write(aLine[col] + '\n')
