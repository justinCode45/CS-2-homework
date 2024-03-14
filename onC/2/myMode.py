import statistics


def mode(aList):
    aDict = {}
    for i in aList:
        aDict[i] = aDict.get(i, 0) + 1
    valueList = aDict.values()
    highestF = max(valueList)

    modeList = []
    for key, value in aDict.items():
        if value == highestF:
            modeList.append(key)

    return modeList


list1 = [1, 1, 4, 5, 6, 2, 4, 7, 1, 4, 6, 1]
print(mode(list1))
print(statistics.multimode(list1))

list2 = [12, 12, 12, 6, 6, 3, 3, 3, 4, 4, 1, 1, 1, 4, 4, 8, 8, 8, 8]
print(mode(list2))
print(statistics.multimode(list2))
