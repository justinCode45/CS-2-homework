import csv

def makeDataList():
    dataList = []
    with open("query.csv","r",encoding="utf8") as inFile:
        theReader = csv.reader(inFile)
        theTitle = next(theReader)
        col = 0 
        while theTitle[col] != 'mag':
            col += 1
        for aLine in theReader:
            dataList.append(float(aLine[col]))
    print(dataList)
    return dataList

makeDataList()