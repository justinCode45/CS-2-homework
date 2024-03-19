
def ferquencyTable(aList):
    aDict = {}

    for i in aList:
        aDict[i] = aDict.get(i,0) +1

    itemList = list(aDict.keys())
    itemList.sort()
    print("TIME","FREQUENCY")
    for item in itemList:
        print(f"{item:4}{aDict[item]:5}")

myList = [12,12,12,6,6,3,3,3,4,4,1,1,1,4,4,8,8,8,8]

ferquencyTable(myList)
    