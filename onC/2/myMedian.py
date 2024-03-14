import statistics

def median(numList):
    copyList = numList[:]
    copyList.sort()
    mid = len(copyList) // 2
    if len(copyList) % 2 == 0:
        medianV = (copyList[mid - 1] + copyList[mid]) / 2
    else:
        medianV = copyList[mid]
    return medianV


eps7 = [37, 32, 46, 28, 37, 41, 31]
eps8 = [37, 32, 46, 28, 37, 41, 31, 29]

print(median(eps7))
print(statistics.median(eps7))

print(median(eps8))
print(statistics.median(eps8))