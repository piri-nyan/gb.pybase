print("Traffic lights")

import time

class TrafficLight():
    def __init__(self, color="red"):
        self.__color = color

    def sleep_in_s(self, s):
        for i in range(0,s):
            print("|", end=" ", flush=True)
            time.sleep(1)
        print("\n")

    @property
    def colour(self):
        return self.__color

    @colour.setter
    def colour(self, color):
        self.__color = "yellow"
        print(self.__color)
        self.sleep_in_s(2)
        self.__color = color
        print(self.__color)

    def running(self):
        print(self.__color)
        for i in range(0,1):
            if self.__color == "red":
                self.sleep_in_s(7)
                self.colour = "green"
            if self.__color == "green":
                self.sleep_in_s(5)
                self.colour = "red"
                

light = TrafficLight(color="green")
print("Setting color with setter")
light.colour = "red"
print("Free running lights for 2 switches (cycles)")
light.running()