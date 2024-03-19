with open("rainFail.txt", "r") as file:
    for aline in file:
        datas = aline.split()
        print(datas)
        print(datas[0], "had", datas[0], "mm os rain.")

with open("rainFail.txt","r") as file:
    with open("report.txt","w") as outfile:
        for aLine in file:
            datas = aLine.split()
            outfile.write(datas[0] + " had " + datas[1] + " mm of rain.\n")
