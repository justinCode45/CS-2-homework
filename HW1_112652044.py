# File Name : HW1_112652044.py
# Author : Justin Chen
# Email Address : justin.sc12@nycu.edu.tw
# HW Number : 1
# Description : This program will draw a square with turtle and the size of the square will be 50 and 60.
# Last Changed : 2024/2/24


import turtle
from turtle import Turtle
import math
from math import cos, sin
import cv2
import numpy as np
import random
import time
import numpy.typing as npt
import cProfile
import threading
import queue



SCREEN_WIDTH = 1580
SCREEN_HEIGHT = 720


    

def canvasLine(canvas, start, end, color,w=1, tag=None):
    canvas.create_line(start[0], start[1], end[0], end[1], fill=color, width=w,tags=tag)

def setupScreen() -> None:
    screen = turtle.Screen()
    screen.screensize(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.setworldcoordinates(0,SCREEN_HEIGHT,SCREEN_WIDTH,0)

def drawSquare(t: Turtle, o: tuple[float], r: tuple[float]) -> None:
    moveTurtle(t, o)
    t.goto(r[0],o[1])
    t.goto(r)
    t.goto(o[0],r[1])
    t.goto(o)
    t.up()    

def drawDivider(t: Turtle) -> None:
    drawSquare(t, (0,0), (SCREEN_WIDTH, SCREEN_HEIGHT))
    moveTurtle(t, (0, SCREEN_HEIGHT//3))
    t.goto(300, SCREEN_HEIGHT//3)
    moveTurtle(t, (0, 2*SCREEN_HEIGHT//3))
    t.goto(300, 2*SCREEN_HEIGHT//3)
    moveTurtle(t, (300, 0))
    t.goto(300, SCREEN_HEIGHT)

def moveTurtle(t: Turtle, dest: npt.ArrayLike) -> None:

    if t._drawing :
        t._newLine()
        t._drawing = False
    t._update()

    t.goto(dest)
    
    t._newLine()
    t._drawing = True
    t._update()

def peanoCurve(t: Turtle, dirction: bool, order: int, length: float) -> None:
    '''
    Draw a Peano curve using turtle graphics.

    Parameters:
    t (Turtle): The turtle object used for drawing.
    dirction (bool): The direction of the curve. 1 for right, 0 for left.
    order (int): The order of the curve. Determines the complexity of the curve.
    length (float): The length of each segment of the curve.

    Returns:
    None
    '''
    mapD = lambda x: 1 if x else -1

    if order == 1: 
        t.forward(length)
        t.right(90 * mapD(dirction))
        t.forward(length)
        t.right(90 * mapD(dirction))
        t.forward(length)
        return
    
    d = 2.6
    forwardLen = length / (d ** (order - 1))

    peanoCurve(t, not dirction, order - 1, length / d)
    if order % 2 == 0:
        t.right(90 * mapD(dirction))
        t.forward(forwardLen)
    else:
        t.forward(forwardLen)
        t.right(90 * mapD(dirction))
    peanoCurve(t, dirction, order - 1, length / d)
    if order % 2 == 0:
        t.left(90 * mapD(dirction))
        t.forward(forwardLen)
        t.left(90 * mapD(dirction))
    else: 
        t.forward(forwardLen)
    peanoCurve(t, dirction, order - 1, length / d)
    if order % 2 == 0:
        t.forward(forwardLen)
        t.right(90 * mapD(dirction))
    else:
        t.right(90 * mapD(dirction))
        t.forward(forwardLen)
    peanoCurve(t, not dirction, order - 1, length / d)

def cardioid(t: Turtle, r: float, n: int, v: int = 2) -> None:
    '''
    Draw a cardioid using turtle graphics.

    Parameters:
    t (Turtle): The turtle object used for drawing.
    r (float): The radius of the cardioid.
    n (int): The number of points used to draw the cardioid.

    Returns:
    None
    '''
    w = 2 * math.pi / n
    origin = t.pos()-(r, 0)
    suporigin = lambda t: origin + (2*r*cos(w*t), 2*r*sin(w*t))
    turtlepos = lambda t: suporigin(t) + (r*cos(v*w*t+math.pi), r*sin(v*w*t+math.pi))
    for i in range(n):
        t.goto(turtlepos(i+1))

def drawequilateralTriangle(t: Turtle, r: float) -> None:
    o = t.pos()
    t.goto(o[0]+r, o[1])
    t.goto(o[0]+r/2, o[1]-r*math.sqrt(3)/2)
    t.goto(o)

def randomPointonRect(o: tuple[float], r: tuple[float]) -> npt.ArrayLike:
    # generate a random point on the rectangle side 
    # o: origin, r: right top
    # return: (x, y)
    w = r[0] - o[0]
    h = r[1] - o[1]
    if random.random() < w / (w + h):
        # w
        return np.array([random.uniform(o[0], r[0]), random.choices([o[1], r[1]])[0]])
    else:
        return np.array([random.choices([o[0], r[0]])[0], random.uniform(o[1], r[1])])

def GaussianKernel(size: int, sigma: float) -> np.ndarray:
    '''
    Generate a Gaussian kernel.

    Parameters:
    size (int): The size of the kernel.
    sigma (float): The standard deviation of the Gaussian distribution.

    Returns:
    np.ndarray: The generated Gaussian kernel.
    '''
    kernel = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            kernel[i][j] = math.exp(-((i-size//2)**2+(j-size//2)**2)/(2*sigma**2))
    return kernel / kernel.sum()

def drawDetailInBox(t: Turtle, img: np.ndarray, o: npt.ArrayLike, r: npt.ArrayLike, torigin: npt.ArrayLike) -> None:
    
    for _ in range(100) :
        p1 = randomPointonRect(o, r)
        p2 = randomPointonRect(o, r)
        if (p1[0] - p2[0]) * (p1[1] - p2[1]) == 0:
            continue
        moveTurtle(t, p1)
        t.setheading( t.towards(p2[0],p2[1]))
        delta = 5
        t.pensize(2)
        step = np.array([0.5*delta*cos(t.heading()), 0.5*delta*sin(t.heading())])
        while 1 :
            tpos = np.array(t.pos())
            samplePoint = tpos + step
            if samplePoint[0] > r[0] or samplePoint[0] < o[0] or samplePoint[1] > r[1] or samplePoint[1] < o[1]:
                break
            samplePoint = samplePoint - torigin
            samplePoint = samplePoint.astype(int)
            if samplePoint[0] > img.shape[1]-1 or samplePoint[1] > img.shape[0]-1 or samplePoint[0] <= 0 or samplePoint[1] <= 0:
                break
            color = img[samplePoint[1]][samplePoint[0]]
            t.color(color[2], color[1], color[0])
            t.forward(delta)

def cavanDrawDetailInBox(c, img: np.ndarray, o: npt.ArrayLike, r: npt.ArrayLike, torigin: npt.ArrayLike) -> None:
    
    for i in range(100):
        p1 = randomPointonRect(o, r)
        p2 = randomPointonRect(o, r)
        if (p1[0] - p2[0]) * (p1[1] - p2[1]) == 0:
            continue
        
        directionVec = (p2 - p1)
        directionVec = directionVec / np.linalg.norm(directionVec)
        delta = 5 
        # t.pensize(16*(1.2-(i/itterGen)**2.2))
        step = directionVec * delta/2

        while 1 :
            samplePoint =  p1 + step
            if samplePoint[0] > r[0] or samplePoint[0] < o[0] or samplePoint[1] > r[1] or samplePoint[1] < o[1]:
                break
            samplePoint = samplePoint - torigin
            samplePoint = samplePoint.astype(int)
            if samplePoint[0] > img.shape[1]-1 or samplePoint[1] > img.shape[0]-1 or samplePoint[0] <= 0 or samplePoint[1] <= 0:
                break
            color = img[samplePoint[1]][samplePoint[0]]
            canvasLine(c, p1, p1+2*step, "#%02x%02x%02x" % (color[2], color[1], color[0]))
            p1 = p1 + 2*step
        # print (i)
            
def getDetailImg(img: np.ndarray) -> np.ndarray:
    ## fft
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)

    rows, cols = img.shape
    crow,ccol = rows//2 , cols//2
    fshift[crow-30:crow+30, ccol-30:ccol+30] = 0
    
    # idft
    f_ishift = np.fft.ifftshift(fshift)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)

    cv2.imwrite("fliter0.jpg", img_back)

    ## Gaussian blur
    kernel = GaussianKernel(5, 1)
    imgG = cv2.filter2D(img_back, -1, kernel)

    return imgG

def drawImage(t: Turtle, path: str) -> None:
   
    t.setundobuffer(None)
    print ("Start")
    # load image , resize , Gaussian blur
    img = cv2.imread(path)
    sH = (720) / img.shape[0]
    sW = (1280) / img.shape[1]  
    scaler = sW if sW < sH else sH 
    img = cv2.resize(img,None,fx=scaler, fy=scaler, interpolation = cv2.INTER_CUBIC)
    img = cv2.filter2D(img, -1, GaussianKernel(5, 1))

    # compute the position of the image
    torigin = np.array([0,0])
    tmax = np.array([0,0])
    if sH < sW : # W  ss
        torigin = np.array([300 + (1280-img.shape[1])/2, 0])
        tmax = torigin + np.array([img.shape[1], 720])
    else: # H ss
        torigin = np.array([300,(720-img.shape[0])/2])
        tmax = torigin + np.array([1580, img.shape[0]])

    ## get detail image
    imgG = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgG = getDetailImg(imgG)
    
    turtle.tracer(10000 ,0)
    starTime = time.time()
    
    # draw the image
    itterGen = 100
    for i in range(itterGen):
        p1 = randomPointonRect(torigin, tmax)
        p2 = randomPointonRect(torigin, tmax)
        if (p1[0] - p2[0]) * (p1[1] - p2[1]) == 0:
            continue
        moveTurtle(t, p1)
        t.setheading( t.towards(p2[0],p2[1]) )
        delta = 5 
        t.pensize(16*(1.2-(i/itterGen)**2.2))
        step = np.array([0.5*delta*cos(t.heading()), 0.5*delta*sin(t.heading())])
        while 1 :
            tpos = np.array(t.pos())
            samplePoint =  tpos + step
            samplePoint = np.clip(samplePoint, torigin, tmax)
            if np.array_equal(samplePoint, torigin) or np.array_equal(samplePoint, tmax):
                break
            samplePoint = samplePoint - torigin
            samplePoint = samplePoint.astype(int)
            if samplePoint[0] > img.shape[1]-1 or samplePoint[1] > img.shape[0]-1 or samplePoint[0] <= 0 or samplePoint[1] <= 0:
                break
            color = img[samplePoint[1]][samplePoint[0]]
            t.color(color[2], color[1], color[0])
            t.forward(delta)

    turtle.update()
    end1 = time.time()
    print("First part done")

    # draw the detail
    detial_size = 20
    for i in range(100):
        maxidx = imgG.argmax()
        maxidx = np.unravel_index(maxidx, imgG.shape)
        obox = np.array([maxidx[1]-detial_size/2, maxidx[0]-detial_size/2])
        rbox = np.array([maxidx[1]+detial_size/2, maxidx[0]+detial_size/2])
        
        obox[0] = max(0, min(obox[0], imgG.shape[1]))
        obox[1] = max(0, min(obox[1], imgG.shape[0]))
        rbox[0] = max(0, min(rbox[0], imgG.shape[1]))
        rbox[1] = max(0, min(rbox[1], imgG.shape[0]))

        imgG[int(obox[1]):int(rbox[1]), int(obox[0]):int(rbox[0])] = 0
        obox += torigin
        rbox += torigin
        drawDetailInBox(t, img, obox, rbox, torigin)

    turtle.update()    
    # reste the pen size end or function
    t.pensize(1)
    endTime = time.time()
    print ("Image time used  : ",end1 - starTime)
    print ("Detail time used : ",endTime - end1)
    print ("Tatle time used  : ",endTime - starTime)
    print("Done")

def canvasDrawImage(c , path: str) -> None:
    
    # load image , resize , Gaussian blur
    img = cv2.imread(path)
    sH = (720) / img.shape[0]
    sW = (1280) / img.shape[1]  
    scaler = sW if sW < sH else sH 
    img = cv2.resize(img,None,fx=scaler, fy=scaler, interpolation = cv2.INTER_CUBIC)
    img = cv2.filter2D(img, -1, GaussianKernel(5, 1))

    # compute the position of the image
    torigin = np.array([0,0])
    tmax = np.array([0,0])
    if sH < sW : # W  ss
        torigin = np.array([300 + (1280-img.shape[1])/2, 0])
        tmax = torigin + np.array([img.shape[1], 720])
    else: # H ss
        torigin = np.array([300,(720-img.shape[0])/2])
        tmax = torigin + np.array([1580, img.shape[0]])

    ## get detail image
    imgG = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgG = getDetailImg(imgG)
    

    starTime = time.time()
    
    # draw the image
    itterGen = 3000
    for i in range(itterGen):
        p1 = randomPointonRect(torigin, tmax)
        p2 = randomPointonRect(torigin, tmax)
        if (p1[0] - p2[0]) * (p1[1] - p2[1]) == 0:
            continue
        
        directionVec = (p2 - p1)
        directionVec = directionVec / np.linalg.norm(directionVec)
        delta = 5 
        step = directionVec * delta/2

        while 1 :
            samplePoint =  p1 + step
            samplePoint = np.clip(samplePoint, torigin, tmax)
            if np.array_equal(samplePoint, torigin) or np.array_equal(samplePoint, tmax):
                break
            samplePoint = samplePoint - torigin
            samplePoint = samplePoint.astype(int)
            if samplePoint[0] > img.shape[1]-1 or samplePoint[1] > img.shape[0]-1 or samplePoint[0] <= 0 or samplePoint[1] <= 0:
                break
            color = img[samplePoint[1]][samplePoint[0]]
            canvasLine(c, p1, p1+2*step, "#%02x%02x%02x" % (color[2], color[1], color[0]), (16*(1.2-(i/itterGen)**2.2)))
            p1 = p1 + 2*step

        if i % 50 == 0:
            c.update()  

    end1 = time.time()
    # draw the detail
    detial_size = 20
    for i in range(50):
        maxidx = imgG.argmax()
        maxidx = np.unravel_index(maxidx, imgG.shape)
        obox = np.array([maxidx[1]-detial_size/2, maxidx[0]-detial_size/2])
        rbox = np.array([maxidx[1]+detial_size/2, maxidx[0]+detial_size/2])

        obox[0] = max(0, min(obox[0], imgG.shape[1]))
        obox[1] = max(0, min(obox[1], imgG.shape[0]))
        rbox[0] = max(0, min(rbox[0], imgG.shape[1]))
        rbox[1] = max(0, min(rbox[1], imgG.shape[0]))

        imgG[int(obox[1]):int(rbox[1]), int(obox[0]):int(rbox[0])] = 0
        obox += torigin
        rbox += torigin
        cavanDrawDetailInBox(c, img, obox, rbox, torigin)

    # reste the pen size end or function
    endTime = time.time()
    print ("Image time used  : ",end1 - starTime)
    print ("Detail time used : ",endTime - end1)
    print ("Tatle time used  : ",endTime - starTime)
    print ("Done")

    root.after(0, animetion, c)

def drawImPixel(t: Turtle,path :str) -> None:

    t.setundobuffer(None)
    img = cv2.imread(path)
    sH = (720) / img.shape[0]
    sW = (1280) / img.shape[1]  
    scaler = sW if sW < sH else sH 
    img = cv2.resize(img,None,fx=scaler, fy=scaler, interpolation = cv2.INTER_CUBIC)

    torigin = np.array([0,0])
    tmax = np.array([0,0])
    if sH < sW : # W  ss
        torigin = np.array([300 + (1280-img.shape[1])/2, 0])
        tmax = torigin + np.array([img.shape[1], 720])
    else: # H ss
        torigin = np.array([300,(720-img.shape[0])/2])
        tmax = torigin + np.array([1580, img.shape[0]])

    turtle.tracer(10000 ,0)

    moveTurtle(t, torigin)

    start = time.time()

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            color = img[i][j]
            t.color(color[2], color[1], color[0])
            t.begin_fill()
            moveTurtle(t, torigin+(j,i))
            t.goto(torigin[0]+j, torigin[1]+i+1)
            t.goto(torigin[0]+j+1, torigin[1]+i+1)
            t.goto(torigin[0]+j+1, torigin[1]+i)
            t.end_fill()
    
    end = time.time()

    print("Time used : ", end - start)

def animetion(c) -> None:
    a = 90
    obj = [ np.array([0,a]), 
            np.array([a*math.sqrt(3)/2,-a/2]), 
            np.array([-a*math.sqrt(3)/2,-a/2])]
    theta = 0.2
    rotateMat = np.array([[cos(theta),-sin(theta)],[sin(theta),cos(theta)]])
    c.create_oval(150-90, 590-90, 150+90, 590+90)

    def _animate(obj=obj, rotateMat=rotateMat):
        obj = [rotateMat @ i for i in obj]
        coorobj = [i + np.array([150, 590]) for i in obj]
        c.delete("anime")
        canvasLine(c, coorobj[0], coorobj[1], "#000000", 2, "anime")
        canvasLine(c, coorobj[1], coorobj[2], "#000000", 2, "anime")
        canvasLine(c, coorobj[2], coorobj[0], "#000000", 2, "anime")
        c.update()
        root.after(300, _animate, obj, rotateMat)

    root.after(0, _animate, obj, rotateMat)


    
def main():
    
    print ("If the program is not responding, please wait for a while, the program is drawing the image.")
    print ("When after the image is drawn, the program will play the animation.")
    print ("Exit the program by closing the window. If it is not responding, please use ctrl+c to terminate the program.")

    random.seed(time.time())
    setupScreen()

    t = Turtle()
    turtle.tracer(30, 1)
    turtle.colormode(255)
    t.setundobuffer(None)
    
    drawDivider(t)

    moveTurtle(t, (55, 220))
    peanoCurve(t, 1, 5, 300)

    moveTurtle(t, (230, 360))
    cardioid(t, 40, 500,2)



    turtle.update()

    # drawImage(t, "fr.jpg")
    # drawImPixel(t, "fr.jpg")
    # cProfile.run('drawIm()','output.pstats')


    # root.after(0, canvasDrawImage, canvas, "fr.jpg")
    root.after(0, animetion, canvas)
    turtle.done()




if __name__ == "__main__":
    canvas = turtle.getcanvas()
    root = canvas.winfo_toplevel()

    main()
