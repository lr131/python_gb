from abc import ABC, abstractmethod


class Clothes(ABC):
    """Абстрактный базовый класс одежды"""
    def __init__(self, name, param):
        self.name = name
        self._param = param

    def __str__(self):
        return self.name

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    """Класс Пальто"""
    @property
    def consumption(self):
        return self._param / 6.5 + 0.5

    @property
    def size(self):
        return self._param


class Costume(Clothes):
    """Класс Костюма"""
    @property
    def consumption(self):
        return self._param * 2 + 0.3

    @property
    def height(self):
        return self._param
