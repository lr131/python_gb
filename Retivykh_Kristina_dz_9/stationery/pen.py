from stationery.stationery import Stationery


class Pen(Stationery):
    def __int__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Запуск отрисовки класса {type(self)} объекта {self.title}")
