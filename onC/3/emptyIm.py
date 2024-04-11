from image import *

sideLength = 300
myWin = ImageWin(sideLength,sideLength,"____'s Line Image")
lineImage = EmptyImage(sideLength,sideLength)

redPixel = Pixel(255,0,0)
for i in range(sideLength):
    lineImage.setPixel(i,i,redPixel)

lineImage.draw(myWin)
# lineImage.save("test.gif")
myWin.exit_on_click()