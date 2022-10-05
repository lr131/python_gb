from equipment import Equipment


class Printer(Equipment):
    """Класс Сканнер
    @:param serial серийный номер
    @:param year Год выпуска
    @:param company Компания
    @:param model Модель
    @:param subtype Подвид принтера: либо принтер, либо плоттер, либо фотопринтер
    @:param printing_type Цветной либо монохромный
    @:param method Метод печати: струйный, матричный, лазерный
    @:param os_compatibility Совместимость с ОС
    @:param is_duplex Есть ли двусторонняя печать
    """
    def __init__(self, serial, year, company, model, subtype,
                 printing_type, method, os_compatibility, is_duplex=False):
        super().__init__(serial, year, company, model, subtype)
        self.printing_type = printing_type 
        self.method = method 
        self.os_compatibility = os_compatibility 
        self.is_duplex = is_duplex 
    
    def __eq__(self, other):
        if not isinstance(other, Printer):
            return False
    
        if ((self.serial == other.serial)
            and (self.year == other.year)
            and (self.company == other.company)
            and (self.model == other.model)
            and (self.subtype == other.subtype)
            and (self.printing_type == other.printing_type)
            and (self.method == other.method)
            and (self.os_compatibility == other.os_compatibility)
            and (self.is_duplex == other.is_duplex)):
                return True
        return False
    
    def to_dict(self):
        return {
            'class': type(self),
            'serial': self.serial,
            'year': self.year,
            'company': self.company,
            'model': self.model,
            'subtype': self.subtype,
            'printing_type': self.printing_type,
            'method': self.method,
            'os_compatibility': self.os_compatibility,
            'is_duplex': self.is_duplex
        }