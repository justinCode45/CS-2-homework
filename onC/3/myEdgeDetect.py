from image import *
import math

def grayPixel(p: Pixel) -> Pixel:
    gray = (p.getRed() + p.getGreen() + p.getBlue()) // 3
    return Pixel(gray, gray, gray)



def pixelMapper(sorceImage: Image, func) -> Image:
    width = sorceImage.getWidth()
    height = sorceImage.getHeight()
    targetImage = EmptyImage(width, height)
    for x in range(width):
        for y in range(height):
            oldPixel = sorceImage.getPixel(x, y)
            newPixel = func(oldPixel)
            targetImage.setPixel(x, y, newPixel)
    return targetImage



def convolve(anImage: Image,r,c,mask):
    sum = 0 
    for row in range(r-1,r+2):
        for col in range(c-1,c+2):
            apixel = anImage.getPixel(col,row)
            intensity = apixel.getRed()
            sum = sum + intensity * mask[row-r+1][col-c+1]
    return sum

def edgeDetect(anImage: Image):
    newImage = EmptyImage(anImage.getWidth(),anImage.getHeight())
    Xmask = [[-1,0,1],[-2,0,2],[-1,0,1]]
    Ymask = [[-1,-2,-1],[0,0,0],[1,2,1]]
    for row in range(1,anImage.getHeight()-1):
        for col in range(1,anImage.getWidth()-1):
            Xsum = convolve(anImage,row,col,Xmask)
            Ysum = convolve(anImage,row,col,Ymask)
            sum = int(math.sqrt(Xsum**2 + Ysum**2))
            if sum > 175:
                newImage.setPixel(col,row,Pixel(0,0,0))
            else:
                newImage.setPixel(col,row,Pixel(255,255,255))
    return newImage
    

def drawResult(oldimage,grayimage,edgeimage):
    width = oldimage.getWidth()
    height = oldimage.getHeight()
    myWin = ImageWin(width*3,height,"Edge Detection")
    oldimage.setPosition(0,0)
    grayimage.setPosition(width,0)
    edgeimage.setPosition(width*2,0)
    oldimage.draw(myWin)
    grayimage.draw(myWin)
    edgeimage.draw(myWin)
    myWin.exitOnClick()


oldImage = FileImage("lcastle.gif")
grayImage = pixelMapper(oldImage, grayPixel)
edgeImage = edgeDetect(grayImage)
drawResult(oldImage,grayImage,edgeImage)
