from equipment import Equipment


class Scanner(Equipment):
    def __init__(self, serial, year, company, model, subtype,
                 light_source, output_file_formats, os_compatibility, speed):
        super().__init__(serial, year, company, model, subtype)
        self.light_source = light_source
        self.speed = speed
        self.output_file_formats = output_file_formats
        self.os_compatibility = os_compatibility
