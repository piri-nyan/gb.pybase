print("Road calculator")

class Road():
    def __init__(self, width, length):
        self.__width = width
        self.__length = length
        self.__weight = 25
        self.__height = 5

    def mass(self):
        return self.__length*self.__width*self.__weight*self.__height

road = Road(20, 5000)
print(road.mass())