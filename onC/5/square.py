
from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, s) -> None:
        super().__init__(s, s)

        print("width=")
        print("height=")

        print("width=", super().getWidth())
        print("height=", super().getHeight())

        print("width=", self.__width)
        print("height=", self.__height)

        print("width=", super.__width)
        print("height=", super.__height)





