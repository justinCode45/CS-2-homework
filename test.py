import sys

# n dim point with l2 dist


class Point:
    def __init__(self, coords):
        self.coords = coords
        self.dim = len(coords)

    def dist(self, other: "Point"):
        sum = 0
        for i in range(len(self.coords)):
            sum += (self.coords[i] - other.coords[i]) ** 2
        return sum ** 0.5

    def __str__(self):
        return str(self.coords)


def readFile(path):
    file = open(path, 'r')
    data = file.read()
    file.close()
    return data


data = readFile("data.txt")
data = data.split("\n")
data = [list(map(float, x.split())) for x in data]
points = [Point(x) for x in data]

k = int(input("Enter the number of clusters: "))
clusters = [[] for i in range(k)]
centroids = [points[i] for i in range(k)]

for aPass in range(100):
    for p in points:
        minDist = float('inf')
        cluster = -1
        for i in range(k):
            dist = p.dist(centroids[i])
            if dist < minDist:
                minDist = dist
                cluster = i
        clusters[cluster].append(p)
    for i in range(k):
        center = Point([0] * points[0].dim)
        for p in clusters[i]:
            for j in range(p.dim):
                center.coords[j] += p.coords[j]
        for j in range(center.dim):
            if len(clusters[i]) != 0:
                center.coords[j] /= len(clusters[i])
        centroids[i] = center
    for cluster in clusters:
        print(cluster)
    print()