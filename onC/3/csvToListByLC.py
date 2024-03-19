import csv


def makeDataList():

    with open("query.csv", "r", encoding="utf8") as inFile:
        theReader = csv.reader(inFile)
        theTitle = next(theReader)
        col = 0
        while theTitle[col] != 'mag':
            col += 1
        dataList = [float(aLine[col]) for aLine in theReader]
    print(dataList)
    return dataList


makeDataList()
