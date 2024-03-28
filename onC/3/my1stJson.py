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