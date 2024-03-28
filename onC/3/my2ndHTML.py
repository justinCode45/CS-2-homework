import urllib.request

url = "https://timetable.nycu.edu.tw"

thePage = urllib.request.urlopen(url)

for i  in range(3):
    linea = thePage.readline()
    print(f"{i}a : {linea}")
    lineb = linea.decode("utf8")
    print(f"{i}b : {lineb}")