import urllib.request

url = "https://timetable.nycu.edu.tw"

thePage = urllib.request.urlopen(url)
print(thePage)
theText = thePage.read().decode("utf8")
print(theText)