from image import *


def convolution(image:Image, kernel:list[list[float]]) -> Image:
    print("Convolution")
            
    result =EmptyImage(image.width, image.height)
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
                    pixel = image.getPixel(row-len(kernel)//2+i, col-len(kernel)//2+j)
                    red += pixel.red * kernel[i][j]
                    green += pixel.green * kernel[i][j]
                    blue += pixel.blue * kernel[i][j]
            #normalize color
            red = int(min(255, max(0, red)))
            green = int(min(255, max(0, green)))
            blue = int(min(255, max(0, blue)))
            result.setPixel(row, col, Pixel(red, green, blue))
            print(f"({row}, {col}) = ({red}, {green}, {blue})")
    return result

def resize(image:Image, width:int, height:int) -> Image:
    result = EmptyImage(width, height)
    for row in range(width):
        for col in range(height):
            x = row * image.width // width
            y = col * image.height // height
            result.setPixel(row, col, image.getPixel(x, y))
    return result

def main():
    image = Image("test.gif")
    image = resize(image, image.width//2, image.height//2)
    win = ImageWin(image.width*2, image.height)
    kernel = [[0, -1, 0], [-1, 5, -1], [0, -1, 0]]
    burlk = [[1, 2, 1], [2, 1, 2], [1, 2, 1]]
    # image = resize(image, image.width//2, image.height//2)
    result = convolution(image, kernel)
    image.draw(win)
    result.setPosition(image.width, 0)
    result.draw(win)
    win.exitOnClick()

if __name__ == "__main__":
    main()