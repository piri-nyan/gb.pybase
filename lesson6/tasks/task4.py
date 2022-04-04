print("Car types with speed limits")

class Car():
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Car goes")

    def stop(self):
        print("Car stops")

    def turn(self, direction):
        print(f"Car turns {direction}")

    def show_speed(self):
        print(self.speed)

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f"{self.speed}, {self.name} превышение скорости!"

class SportCar(Car):
    def __init__(self):
        return super().__init__()

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f"{self.speed}, {self.name} превышение скорости!"

class PoliceCar(Car):
    def __init__(self):
        return super().__init__()

tc = TownCar(61, "red", "Town Car 1", False)
print(tc.show_speed())

wc = WorkCar(41, "green", "Work Car 1", False)
print(wc.show_speed())