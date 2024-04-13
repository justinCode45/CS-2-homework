from image import *


def mirrorX(image: Image) -> Image:
    result = EmptyImage(image.width, image.height)
    for row in range(image.width):
        for col in range(image.height):
            result.setPixel(row, col, image.getPixel(row, image.height-col-1))
    return result


def mirrorY(image: Image) -> Image:
    result = EmptyImage(image.width, image.height)
    for row in range(image.width):
        for col in range(image.height):
            result.setPixel(row, col, image.getPixel(image.width-row-1, col))
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
    for row in range(image.width):
        for col in range(image.height):
            result.setPixel(row, col, image.getPixel(row, col))
    for row in range(len(kernel)//2, image.width-len(kernel)//2):
        for col in range(len(kernel)//2, image.height-len(kernel)//2):
            red = 0
            green = 0
            blue = 0
            for i in range(len(kernel)):
                for j in range(len(kernel)):
                    pixel = image.getPixel(
                        row-len(kernel)//2+i, col-len(kernel)//2+j)
                    red += pixel.red * kernel[i][j]
                    green += pixel.green * kernel[i][j]
                    blue += pixel.blue * kernel[i][j]
            # make sure the value is in the range of 0-255
            red = int(min(255, max(0, red)))
            green = int(min(255, max(0, green)))
            blue = int(min(255, max(0, blue)))
            result.setPixel(row, col, Pixel(red, green, blue))
    return result


def resize(image: Image, width: int, height: int) -> Image:
    result = EmptyImage(width, height)
    for row in range(width):
        for col in range(height):
            x = row * image.width // width
            y = col * image.height // height
            result.setPixel(row, col, image.getPixel(x, y))
    return result


def main():
    filename = input("Enter the image file name: ")
    try:
        image = Image(filename)
    except FileNotFoundError:
        print("File not found.")
        return
    image = resize(image, image.width//3, image.height//3)
    commond = input("Enter the command (v,b,h,s): ")
    for c in commond:
        win = ImageWin(image.width, image.height, "Image")
        if c == 'v':
            result = mirrorX(image)
        elif c == 'h':
            result = mirrorY(image)
        elif c == 'b':
            kernel = [[1, 2, 1], [2, 1, 2], [1, 2, 1]]
            result = convolution(image, kernel)
        elif c == 's':
            kernel = [[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]]
            result = convolution(image, kernel)
        result.draw(win)
        win.exit_on_click()


if __name__ == "__main__":
    main()
