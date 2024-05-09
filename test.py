class Test:
    def __init__(self) -> None:
        # self._Test__name = "tttets"
        self.__name = "miku"
    def getter_name(self):
        return self.__name
    def getter_name2(self):
        print(self.__dict__)
def main():

    t = Test()
    print(t.getter_name())
    t.__name = "Test2"
    print(t.getter_name())
    print(t.getter_name2())
    print(t.__dict__)
    # t.__name = "Test2"
    # print(t.__dict__)
    # print(t.__name) # Test2
    # t._Test__name = "Test3"
    # print(t.__dict__)
    pass 


if __name__ == "__main__":
    main()
    