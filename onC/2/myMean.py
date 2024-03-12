import statistics

def mean(numList):
    meanV = sum(numList) / len(numList)
    return meanV


earthquake = [37, 32, 46, 28, 37, 41, 31]
print(mean(earthquake))
print(statistics.mean(earthquake))