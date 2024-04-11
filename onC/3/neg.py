from image import *

def negativePixel(oldPixel):
    nr = 255 - oldPixel.getRed()
    ng = 255 - oldPixel.getGreen()
    nb = 255 - oldPixel.getBlue()
    return Pixel(nr,ng,nb)


def makeNegative(imagePath):
    oldImage = FileImage(imagePath)
    width = oldImage.getWidth()
    height = oldImage.get_height()
    newImage = EmptyImage(width,height)

    for row in range(height):
        for col in range(width):
            oldPixle = oldImage.getPixel(col,row)
            newPixle = negativePixel(oldPixle)
            newImage.setPixel(col,row,newPixle)

    myWin = ImageWin(width*2,height,"Image Processing")
    oldImage.draw(myWin)
    newImage.setPosition(width,0)
    newImage.draw(myWin)
    myWin.exit_on_click()

makeNegative("lcastle.gif")