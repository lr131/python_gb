from datetime import datetime

from copier import Copier
from scanner import Scanner
from printer import Printer


class Store:
    __logistic = [] # учет отправки,
    # структура: филиал: объект бранч, дата отгрузки, какой объект отправлен
    # self.branch = branch
    # self.__transfer_branch_date = transfer_branch_date

    # тогда надо сделать метод Заказать (и будут ожидаться)
    def __init__(self, temp, humidity, capacity, lst=None):
        self.temp = temp
        self.humidity = humidity
        self.capacity = capacity
        self.__state = Store.list_to_state(lst) # текущее состояние склада
        # __state = {
        #     a: {state: "(ожидается, получен, отправлен)",
        #         "inventory_number": "инвентарный номер",
        #         "reg_date": "дата регистрации"}
        # }
        # объект как ключ, его статус ,

    class State:
        """Состояние содержимого склада на текущий момент"""
        def __init__(self, obj, state, inventory_number=None, reg_date=None):
            """Задает начальное состояние.

            @:param obj объект оргтехники
            @:param state состояние вида 'ожидается', 'получен' или 'отправлен'
            @:param inventory_number инвентарный номер (присваивается при
            поступлении на склад)
            @:param reg_date дата постановки на учет"""
            pass

    @classmethod
    def from_list(cls, t, h, lst):
        return cls(t, h, lst)

    def take(self, equipment):
        pass

    def order(self, equipment):
        pass

    def push(self, equipment, branch):
        pass

    @staticmethod
    def list_to_state(lst):
        # тут будет перевод обычного списка в нормальный словарь
        return {}
