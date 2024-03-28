import json
import urllib.request
import statistics


url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.geojson"
handle = urllib.request.urlopen(url)
print(handle)
jsonData = handle.read()


quakeData = json.loads(jsonData)

print("Keys in quake data:",quakeData.keys(),'\n')

quakeList = quakeData.get("features")
print("Number of quakes:",len(quakeList),'\n')
print("First quake:",quakeList[0],'\n')
keysInQuake = quakeList[0].keys()
print("Keys in a quake:",keysInQuake,'\n')


def makeMagList(quakeData):
    magList = []
    quakeList = quakeData.get("features")
    for quake in quakeList:
        mag = quake.get("properties").get("mag")
        magList.append(mag)
    return magList

magList = makeMagList(quakeData)
print(magList)
print("--------------------------")
print("len of magList:",len(magList))
print("Max of magList:",max(magList))
print("Mean of magList:",statistics.mean(magList))
print("Multimode of magList:",statistics.multimode(magList))