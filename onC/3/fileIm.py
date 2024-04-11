from image import *

myWin = ImageWin(300,200,"________'s Image Processing")
im = FileImage("lcastle.gif")
im.draw(myWin)

width = im.getWidth()
height = im.getHeight()
aPixle = im.getPixel(0,0)
print("Width of image: ", width)
print("Height of image: ", height)
print("Pixel at (0,0)", aPixle)

myWin.exitonclick()
