from cars.car import Car


class TownCar(Car):
    __max_speed = 40

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > self.__max_speed:
            print("Превышение скорости!")
        print(f"Машина {self.name} едет со скоростью {self.speed}")
