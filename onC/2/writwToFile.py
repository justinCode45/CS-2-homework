
with open("rainFail.txt","r") as file:
    with open("report.txt","w") as outfile:
        for aLine in file:
            datas = aLine.split()
            inInch = float(datas[1])/2.54
            outfile.write("%s had %s mm (i.e.,%f inches) of raain.\n" % (datas[0],datas[1],inInch))
            outfile.write("%s had %s mm (i.e.,%.2f inches) of raain.\n" % (datas[0],datas[1],inInch))
            outfile.write("{0} had {1} mm (i.e.,{2:2f} inches) of raain.\n".format(datas[0],datas[1],inInch))
            

