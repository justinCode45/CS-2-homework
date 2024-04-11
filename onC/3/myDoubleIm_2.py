from image import *

def doubleImage(sorceImage: Image):
    width = sorceImage.getWidth()
    height = sorceImage.getHeight()
    newWidth = width * 2
    newHeight = height * 2
    targetImage = EmptyImage(newWidth,newHeight)
    for x in range(newHeight):
        for y in range(newWidth):
            oldPixel = sorceImage.getPixel(y // 2, x // 2)
            targetImage.setPixel(y,x, oldPixel)
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