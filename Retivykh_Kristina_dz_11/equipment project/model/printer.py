from equipment import Equipment


class Printer(Equipment):
    def __init__(self, serial, year, company, model, subtype,
                 printing_type, method, os_compatibility, is_duplex=False):
        super().__init__(serial, year, company, model, subtype)
        self.printing_type = printing_type
        self.method = method
        self.os_compatibility = os_compatibility
        self.is_duplex = is_duplex
