class Road:
    _length = 0
    _width = 0

    def __init__(self, length, width):
        """Объект класса Road

        @:param length длина дороги, м
        @:param width ширина дороги, м"""
        self._length = length
        self._width = width

    def mass_of_asphalt(self, asphalt_mass, thickness):
        """Возвращает требуемую массу асфальта в тоннах.

        @:param asphalt_mass  масса асфальта в кг для покрытия одного кв. метра
        дороги асфальтом, толщиной в 1 см

        @:param thickness  число см толщины полотна"""
        return self._length * self._width * asphalt_mass * thickness / 1000
