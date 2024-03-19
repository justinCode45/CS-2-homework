def makeDataList():
    dataList = []
    with open("mag1.txt","r") as inFile:
        for aLIne in inFile:
            dataList.append(float(aLIne))

    print(dataList)
    return dataList

makeDataList()