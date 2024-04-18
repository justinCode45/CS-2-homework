import random
import math

def readFile(path):
    file = open(path, 'r')
    data = file.read()
    file.close()
    return data

def creatCentroids(k, data):
    centroids = []
    for i in range(k):
        centroid = []
        for j in range(len(data[0])):
            centroid.append(random.uniform(min(data[j]), max(data[j])))
        centroids.append(centroid)
    return centroids

def euclidD(point1, point2):
    sum = 0
    for i in range(len(point1)):
        sum += (point1[i] - point2[i]) ** 2
    return math.sqrt(sum)

def createClusters(k, centroids, data,repeat = 1):
    for aPass in range(repeat):
        print("Pass", aPass)
        clusters = [[] for i in range(k)]
        for point in data:
            minDist = float('inf')
            cluster = -1
            for i in range(k):
                dist = euclidD(point, centroids[i])
                if dist < minDist:
                    minDist = dist
                    cluster = i
            clusters[cluster].append(point)
        for i in range(k):
            sum = [0] * len(data[0])
            for point in clusters[i]:
                for j in range(len(point)):
                    sum[j] += point[j]
            for j in range(len(sum)):
                if len(clusters[i]) != 0:
                    centroids[i][j] = sum[j] / len(clusters[i])
        for cluster in clusters:
            print(cluster)
            for key in cluster:
                print(key)
        print()
    return clusters

k = int(input("Enter the number of clusters: "))

dataDict = readFile("data.txt")
print(dataDict)

centorids = creatCentroids(k, dataDict)
print(centorids)


repate = int(input("Enter the number of repeat: "))
createClusters(k, centorids, dataDict, repate)