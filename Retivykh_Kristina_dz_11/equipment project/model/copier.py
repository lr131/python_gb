from equipment import Equipment


class Copier(Equipment):
    def __init__(self, serial, year, company, model, subtype,
                 copy_cost, method, speed):
        super().__init__(serial, year, company, model, subtype)
        self.copy_cost = copy_cost
        self.speed = speed
        self.method = method
