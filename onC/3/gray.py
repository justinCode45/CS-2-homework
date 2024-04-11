from image import *

def grayPixel(oldPixel):
    avergb = (oldPixel.getRed()+oldPixel.getGreen() +oldPixel.getBlue())//3
    return Pixel(avergb,avergb,avergb)


def makeGrayScale(imagePath):
    oldImage = FileImage(imagePath)
    width = oldImage.getWidth()
    height = oldImage.get_height()
    newImage = EmptyImage(width,height)

    for row in range(height):
        for col in range(width):
            oldPixle = oldImage.getPixel(col,row)
            newPixle = grayPixel(oldPixle)
            newImage.setPixel(col,row,newPixle)

    myWin = ImageWin(width*2,height,"Image Processing")
    oldImage.draw(myWin)
    newImage.setPosition(width,0)
    newImage.draw(myWin)
    myWin.exit_on_click()

makeGrayScale("lcastle.gif")