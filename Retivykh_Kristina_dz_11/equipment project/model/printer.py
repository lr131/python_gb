from equipment import Equipment


class Printer(Equipment):
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