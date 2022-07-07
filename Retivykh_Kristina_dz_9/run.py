from worker import position
from road import Road
from traffic_light import TrafficLight
from cars.towncar import TownCar
from cars.sportcar import SportCar
from cars.workcar import WorkCar
from cars.policecar import PoliceCar
from stationery.pen import Pen
from stationery.pencil import Pencil
from stationery.handle import Handle



if __name__ == '__main__':
    trafficLight = TrafficLight()
    trafficLight.running(2)

    road = Road(20, 5000)
    print(road.mass_of_asphalt(25, 5))

    position = position.Position("Анна", "Матвеева", "Менеджер", 50, 20)
    print(position.get_full_name())
    print(position.get_total_income())

    townCar = TownCar(80, "Красный", "Тойота", False)
    townCar.show_speed()
    sportCar = SportCar(180, "Желтый", "Ferrari", False)
    sportCar.show_speed()
    workCar = WorkCar(90, "Серый", "Хонда", False)
    workCar.show_speed()
    policeCar = PoliceCar(60, "Lada", "Тойота", True)
    policeCar.show_speed()

    pen = Pen()
    pen.draw()
    pencil = Pencil()
    pencil.draw()
    handle = Handle()
    handle.draw()
