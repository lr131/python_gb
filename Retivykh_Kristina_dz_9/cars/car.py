class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f"Машина {self.name} едет со скоростью {self.speed}")
