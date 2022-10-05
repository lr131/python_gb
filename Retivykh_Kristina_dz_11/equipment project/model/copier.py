from . import Equipment


class Copier(Equipment):
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