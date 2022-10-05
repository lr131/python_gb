from equipment import Equipment


class Copier(Equipment):
    """Класс Сканнер
    @:param serial серийный номер
    @:param year Год выпуска
    @:param company Компания
    @:param model Модель
    @:param subtype Тип по принципу сканирования: аналоговый, цифровой
    @:param copy_cost Поддерживаемый формат бумаги: А4, А3, А2
    @:param method Метод печати: струйный, термопечать, сублимации, ударно-красочный
    @:param speed Скорость копирования (копий/мин)
    """
    def __init__(self, serial, year, company, model, subtype,
                 copy_cost, method, speed):
        super().__init__(serial, year, company, model, subtype)
        self.copy_cost = copy_cost
        self.speed = speed
        self.method = method

    def __eq__(self, other):
        if not isinstance(other, Copier):
            return False
    
        if ((self.serial == other.serial)
            and (self.year == other.year)
            and (self.company == other.company)
            and (self.model == other.model)
            and (self.subtype == other.subtype)
            and (self.copy_cost == other.copy_cost)
            and (self.method == other.method)
            and (self.speed == other.speed)):
                return True
        return False