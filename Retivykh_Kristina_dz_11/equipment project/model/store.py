from datetime import datetime
from re import L
import uuid

from copier import Copier
from scanner import Scanner
from printer import Printer
from branch import Branch
from exceptions import OutOfStoreError
from exceptions import NotFoundEquipmentError
from exceptions import LogisticPathEquipmentError


class Store:
    """Класс Склад
    @:param temp средняя температура склада
    @:param humidity средняя влажность склада
    @:param capacity вместимость склада, сколько единиц в него входит
    @:param temp средняя температура склада
    @:param state средняя температура склада
    """
    __logistic = [] # учет движения техники, логистика
    __state = [] # текущее наполнение склада, его состояние


    def __init__(self, temp, humidity, capacity, lst=[]):
        self.temp = temp # средняя температура
        self.humidity = humidity # влажность
        self.capacity = capacity # вместимость
        # state: "(ожидается, получен, отправлен)"

    class State:
        """Состояние содержимого склада на текущий момент"""
        def __init__(self, obj, inventory_number=None, reg_date=None):
            """Задает начальное состояние.
            @:param obj объект оргтехники
            @:param inventory_number инвентарный номер (присваивается при
            поступлении на склад)
            @:param reg_date дата постановки на учет"""
            self.obj = obj
            self.inventory_number = inventory_number
            self.reg_date = reg_date

    @classmethod
    def from_list(cls, t, h, lst):
        return cls(t, h, lst)

    def add(self, equipment, count=1):
        # проверить, заказывали ли
        if (len(self.__state) + count) > self.capacity:
            raise OutOfStoreError
        for k in range(0,count):
            inventory_number = uuid.uuid4()
            self.__logistic.append({'equipment': equipment,
                                    'inventory_number': inventory_number,
                                    'serial': equipment.serial,
                                    'date': datetime.now().date(),
                                    'action': 'получен',
                                    'branch': None})
            self.__state.append(self.State(equipment, inventory_number,
                                    reg_date=datetime.now().date()))

    def order(self, equipment):
        self.__logistic.append({'equipment': equipment,
                                'serial': equipment.serial,
                                'inventory_number': None,
                                'date': None,
                                'action': 'ожидается',
                                'branch': None})
        

    def push(self, equipment, inventory_number, branch):       
        #Удалять из State, в логистике менять 
        state_indx = self.find(inventory_number)
        if state_indx:
            self.__state.pop(state_indx)
            indx = self.find_logistic(inventory_number)
            if indx:
                branch.add(equipment)
                self.__logistic[indx]['action'] = 'отправлен'
            else:
                raise LogisticPathEquipmentError
        else:
            raise NotFoundEquipmentError
    
    def find(self, inventory_number):
        for i, obj in enumerate(self.__state):
            if (obj.inventory_number == inventory_number):
                return i
        return None

    def find_logistic(self, equipment, inventory_number=None):
        if inventory_number:
            for i, obj in enumerate(self.__logistic):
                if (obj.inventory_number == inventory_number):
                    return i
            return None
        
        for i, obj in enumerate(self.__logistic):
            if (obj.equipment == equipment):
                return i
        return None

    @staticmethod
    def list_to_state(lst):
        # тут будет перевод обычного списка в нормальный словарь
        return []
