class Rectangle:
    def __init__(self, w, h) -> None:
        self.__width = w
        self.__height = h

    def getWidth(self):
        return self.__width
    
    def getHeight(self):
        return self.__height
    
    def setWidth(self, w):
        self.__width = w

    def setHeight(self, h):
        self.__height = h