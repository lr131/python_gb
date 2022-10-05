class Equipment:
    """Класс Оргтехника"""
    def __init__(self, serial, year, company, model, subtype):
        self.serial = serial
        self.year = year
        self.company = company
        self.model = model
        self.subtype = subtype

    def __eq__(self, other):
        return False
    
    def to_dict(self):
        return {
            'class': type(self),
            'serial': self.serial,
            'year': self.year,
            'company': self.company,
            'model': self.model,
            'subtype': self.subtype
        }