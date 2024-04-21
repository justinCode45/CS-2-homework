# File Name : HW6_112652044.py
# Author : Justin Chen
# Email Address : justin.sc12@nycu.edu.tw
# HW Number : 6
# Description : This program will process image and compress the image using SVD.
# Last Changed : 2024/4/21
# Dependencies : Python 3.12.2, numpy
# Additional :
#   1. SVD compress function is implemented.
#   2. flipX and flipY function is implemented.

from image import *
isNumPyExist = True

try:
    import numpy as np
except:
    isNumPyExist = False
    print("Please install numpy to enable svdcompress function.")

brulKernel = [[1, 2, 1], [2, 1, 2], [1, 2, 1]]
sharpKernel = [[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]]


def flipX(image: Image) -> Image:
    result = EmptyImage(image.width, image.height)
    for row in range(image.height):
        for col in range(image.width):
            result.setPixel(col, row, image.getPixel(image.width-col-1, row))
    return result


def flipY(image: Image) -> Image:
    result = EmptyImage(image.width, image.height)
    for row in range(image.height):
        for col in range(image.width):
            result.setPixel(col, row, image.getPixel(col, image.height-row-1))
    return result


def mirrorX(image: Image):
    result = image.copy()
    for row in range(image.height):
        for col in range(image.width//2):
            result.setPixel(image.width-col-1, row, image.getPixel(col, row))
    return result


def mirrorY(image: Image):
    result = image.copy()
    for row in range(image.height//2):
        for col in range(image.width):
            result.setPixel(col, image.height-row-1, image.getPixel(col, row))
    return result


def convolution(image: Image, kernel: list[list[float]]) -> Image:
    # normalize kernel
    sum = 0
    for i in range(len(kernel)):
        for j in range(len(kernel)):
            sum += kernel[i][j]
    if sum != 0:
        for i in range(len(kernel)):
            for j in range(len(kernel)):
                kernel[i][j] /= sum

    result = EmptyImage(image.width, image.height)
    for row in range(image.height):
        for col in range(image.width):
            result.setPixel(col, row, image.getPixel(col, row))
    for row in range(len(kernel)//2, image.height-len(kernel)//2):
        for col in range(len(kernel)//2, image.width-len(kernel)//2):
            red = 0
            green = 0
            blue = 0
            for i in range(len(kernel)):
                for j in range(len(kernel)):
                    pixel = image.getPixel(
                        col-len(kernel)//2+j, row-len(kernel)//2+i)
                    red += pixel.red * kernel[i][j]
                    green += pixel.green * kernel[i][j]
                    blue += pixel.blue * kernel[i][j]
            # make sure the value is in the range of 0-255
            red = int(min(255, max(0, red)))
            green = int(min(255, max(0, green)))
            blue = int(min(255, max(0, blue)))
            result.setPixel(col, row, Pixel(red, green, blue))
    return result


def resize(image: Image, width: int, height: int) -> Image:
    result = EmptyImage(width, height)
    for row in range(height):
        for col in range(width):
            x = col * image.width / width
            y = row * image.height / height
            result.setPixel(col, row, image.getPixel(int(x), int(y)))
    return result


def mosaic(image: Image) -> Image:
    result = resize(image, image.width//10, image.height//10)
    result = resize(result, image.width, image.height)
    return result


def svdcompress(image: Image, k: int) -> Image:
    # convert image to matrix
    matrixR = np.zeros((image.height, image.width))
    matrixG = np.zeros((image.height, image.width))
    matrixB = np.zeros((image.height, image.width))
    for row in range(image.height):
        for col in range(image.width):
            pixel = image.getPixel(col, row)
            matrixR[row][col] = pixel.red
            matrixG[row][col] = pixel.green
            matrixB[row][col] = pixel.blue
    # svd
    uR, sR, vhR = np.linalg.svd(matrixR, full_matrices=False)
    uG, sG, vhG = np.linalg.svd(matrixG, full_matrices=False)
    uB, sB, vhB = np.linalg.svd(matrixB, full_matrices=False)
    kR = int(k * len(sR) / 100)
    kG = int(k * len(sG) / 100)
    kB = int(k * len(sB) / 100)
    # compress
    sR[kR:] = 0
    sG[kG:] = 0
    sB[kB:] = 0
    matrixR = np.dot(uR, np.dot(np.diag(sR), vhR))
    matrixG = np.dot(uG, np.dot(np.diag(sG), vhG))
    matrixB = np.dot(uB, np.dot(np.diag(sB), vhB))

    # convert matrix to image
    result = EmptyImage(image.width, image.height)
    for row in range(image.height):
        for col in range(image.width):
            red = int(min(255, max(0, matrixR[row][col])))
            green = int(min(255, max(0, matrixG[row][col])))
            blue = int(min(255, max(0, matrixB[row][col])))
            result.setPixel(col, row, Pixel(red, green, blue))
    return result


def main():

    filename = input("Enter the image file name: ")
    try:
        image = Image(filename)
    except FileNotFoundError:
        print("File not found.")
        return
    image = resize(image, image.width//2, image.height//2)
    commond = input("Enter the command (v,b,h,s,f,g): ")
    image_dict: dict[str, Image] = {}

    for c in commond:

        win = ImageWin(image.width, image.height, "Image")
        if c not in image_dict.keys():

            if c == 'v':
                image_dict[c] = mirrorY(image)
            elif c == 'h':
                image_dict[c] = mirrorX(image)
            elif c == 'b':
                image_dict[c] = convolution(image, brulKernel)
            elif c == 's':
                image_dict[c] = convolution(image, sharpKernel)
            elif c == 'm':
                image_dict[c] = mosaic(image)
            elif c == 'f':
                image_dict[c] = flipX(image)
            elif c == 'g':
                image_dict[c] = flipY(image)
            else:
                continue
        image_dict[c].draw(win)
        win.exit_on_click()

    if not isNumPyExist:
        return
    k = int(input("Enter the compression factor k(1~100):"))
    win = ImageWin(image.width, image.height, "Image")
    result = svdcompress(image, k)
    result.draw(win)
    win.exit_on_click()


if __name__ == "__main__":
    main()
