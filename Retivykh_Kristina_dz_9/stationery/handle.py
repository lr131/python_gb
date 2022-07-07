from stationery.stationery import Stationery


class Handle(Stationery):
    def __int__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Запуск отрисовки {self.title}")
