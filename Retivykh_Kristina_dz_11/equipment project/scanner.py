from equipment import Equipment


class Scanner(Equipment):
    """Класс Сканнер
    @:param serial серийный номер
    @:param year Год выпуска
    @:param company Компания
    @:param model Модель
    @:param subtype Разновидность сканнера: ручной, протяжный, планшетный, слайд-сканнер, проекционный, барабанный
    @:param output_file_formats в каких форматах сохраняет
    @:param os_compatibility Совместимость с ОС
    @:param speed Скорость сканирования
    """
    def __init__(self, serial, year, company, model, subtype,
                 output_file_formats, os_compatibility, speed):
        super().__init__(serial, year, company, model, subtype)
        self.speed = speed
        self.output_file_formats = output_file_formats
        self.os_compatibility = os_compatibility

    def __eq__(self, other):
        if not isinstance(other, Scanner):
            return False
        
        if ((self.serial == other.serial)
            and (self.year == other.year)
            and (self.company == other.company)
            and (self.model == other.model)
            and (self.subtype == other.subtype)
            and (self.output_file_formats == other.output_file_formats)
            and (self.os_compatibility == other.os_compatibility)
            and (self.speed == other.speed)):
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
            'speed': self.speed,
            'output_file_formats': self.output_file_formats,
            'os_compatibility': self.os_compatibility
        }