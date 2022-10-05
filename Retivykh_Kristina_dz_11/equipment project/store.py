from datetime import datetime
import uuid

from equipment import Equipment

from exceptions import OutOfStoreError
from exceptions import NotFoundEquipmentError
from exceptions import LogisticPathEquipmentError


class Store:
    """Класс Склад
    @:param temp средняя температура склада
    @:param humidity средняя влажность склада
    @:param capacity вместимость склада, сколько единиц в него входит
    """
    __logistic = [] # учет движения техники, логистика
    __state = [] # текущее наполнение склада, его состояние


    def __init__(self, temp, humidity, capacity, lst=[]):
        self.temp = temp # средняя температура
        self.humidity = humidity # влажность
        self.capacity = capacity # вместимость

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
        
        def to_dict(self):
            env = self.obj.to_dict()
            env.update({'inventory_number': self.inventory_number,
                    'reg_date': self.reg_date})
            return env
            
        def __str__(self):
            return str(self.to_dict())
            
        @classmethod    
        def state_to_dict(cls, obj):
            env = obj.obj.to_dict()
            env.update({'inventory_number': obj.inventory_number,
                    'reg_date': obj.reg_date})
            return env

    def add(self, equipment):
        if not isinstance(equipment, Equipment):
            raise ValueError("Оборудование должно быть класса Equipment")
        if (len(self.__state) + 1) > self.capacity:
            raise OutOfStoreError
            
        inventory_number = uuid.uuid4()
        state = self.State(obj=equipment, 
                            inventory_number=inventory_number,
                            reg_date=datetime.now().date())
        self.__state.append(state)
        # проверяем, заказывали ли эту единицу оборудования

        i = self.find_logistic(equipment)
        if i:
            self.__logistic[i]['inventory_number'] = inventory_number
            self.__logistic[i]['date'] = datetime.now().date()
            self.__logistic[i]['action'] = 'получен'
        else:
            self.__logistic.append({'equipment': equipment,
                                    'inventory_number': inventory_number,
                                    'serial': equipment.serial,
                                    'date': datetime.now().date(),
                                    'action': 'получен',
                                    'branch': None})

    def order(self, equipment):
        if not isinstance(equipment, Equipment):
            raise ValueError("Оборудование должно быть класса Equipment")
        self.__logistic.append({'equipment': equipment,
                                'serial': equipment.serial,
                                'inventory_number': None,
                                'date': None,
                                'action': 'ожидается',
                                'branch': None})
        

    def push(self, equipment, branch, inventory_number=None):
        if not isinstance(equipment, Equipment):
            raise ValueError("Оборудование должно быть класса Equipment")
        """Метод отгружает оборудование в отделение""" 
        if inventory_number:     
            #Удалять из State, в логистике менять 
            state_indx = self.find(inventory_number)
        else:
            state_indx = self.find(serial=equipment.serial)
        
        if isinstance(state_indx, int) and state_indx >=0:
            self.__state.pop(state_indx)
            if inventory_number:
                indx = self.find_logistic(equipment=equipment, 
                                          inventory_number=inventory_number)
            else:
                indx = self.find_logistic(equipment=equipment,
                                          serial=equipment.serial)

            if isinstance(indx, int) and indx >=0:
                branch.add(equipment)
                self.__logistic[indx]['action'] = 'отправлен'
                self.__logistic[indx]['branch'] = branch.name
            else:
                raise LogisticPathEquipmentError
        else:
            raise NotFoundEquipmentError
        
    
    def find(self, inventory_number=None, serial=None):
        if serial:
            for i, obj in enumerate(self.__state):
                if (obj.obj.serial == serial):
                    return i
        elif inventory_number:    
            for i, obj in enumerate(self.__state):
                if (obj.inventory_number == inventory_number):
                    return i
        return None

    def find_logistic(self, equipment, inventory_number=None, serial=None):
        if inventory_number:
            for i, obj in enumerate(self.__logistic):
                if (obj.get('inventory_number') == inventory_number):
                    return i
            return None
        
        if serial:
            for i, obj in enumerate(self.__logistic):
                if (obj.get('serial') == serial):
                    return i
            return None
                
        for i, obj in enumerate(self.__logistic):
            if (obj.get('equipment') == equipment):
                return i
        return None
    
    @property
    def state(self):
        return [self.State.to_dict(obj) for obj in self.__state]
    
    @property
    def logistic(self):
        res = []
        for obj in self.__logistic:
            res.append(dict(map(lambda x: (x[0], x[1]) if x[0] != 'equipment' else (x[0], x[1].to_dict()), tuple(obj.items()))))
        return tuple(res)
    
    def __str__(self):
        return (f"Характеристики склада:\n"
            f"Средняя температура: {self.temp}\n"
            f"Средняя влажность: {self.humidity}\n"
            f"Вместимость: {self.capacity}\n"
            f"Занято мест: {len(self.__state)}\n")