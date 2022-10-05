from equipment import Equipment


class Scanner(Equipment):
    def __init__(self, serial, year, company, model, subtype,
                 light_source, output_file_formats, os_compatibility, speed):
        super().__init__(serial, year, company, model, subtype)
        self.light_source = light_source
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
            and (self.light_source == other.light_source)
            and (self.output_file_formats == other.output_file_formats)
            and (self.os_compatibility == other.os_compatibility)
            and (self.speed == other.speed)):
                return True
        return False