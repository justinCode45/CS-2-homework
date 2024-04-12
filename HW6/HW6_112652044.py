from image import *


def convolution(image:Image, kernel:list[list[float]]) -> Image:
    result =EmptyImage(image.width, image.height)
    for i in range(image.width):
        for j in range(image.height):
            sum = 0
            for x in range(len(kernel)):
                for y in range(len(kernel[0])):
                    if i+x-len(kernel)//2 >= 0 and i+x-len(kernel)//2 < image.width and j+y-len(kernel[0])//2 >= 0 and j+y-len(kernel[0])//2 < image.height:
                        sum += image[i+x-len(kernel)//2, j+y-len(kernel[0])//2] * kernel[x][y]
            result[i,j] = sum
    return result

def main():
    image = Image("test.jpg")
    kernel = [[0, -1, 0], [-1, 5, -1], [0, -1, 0]]
    result = convolution(image, kernel)
    result.save("output.bmp")

if __name__ == "__main__":
    main()