from image import *

def doubleImage(sorceImage: Image):
    width = sorceImage.getWidth()
    height = sorceImage.getHeight()
    targetImage = EmptyImage(width * 2, height * 2)
    for x in range(width):
        for y in range(height):
            color = sorceImage.getPixel(x, y)
            targetImage.setPixel(x * 2, y * 2, color)
            targetImage.setPixel(x * 2 + 1, y * 2, color)
            targetImage.setPixel(x * 2, y * 2 + 1, color)
            targetImage.setPixel(x * 2 + 1, y * 2 + 1, color)
    return targetImage

def makeDoubleImage(imageFile: str):
    oldImage = FileImage(imageFile)
    oldWeight = oldImage.getWidth()
    oldHeight = oldImage.getHeight()
    newImage = doubleImage(oldImage)

    myWin = ImageWin(oldWeight * 2, oldHeight * 3,"Double Image")
    oldImage.draw(myWin)
    newImage.setPosition(0, oldHeight)
    newImage.draw(myWin)
    myWin.exitOnClick()

makeDoubleImage("lcastle.gif")