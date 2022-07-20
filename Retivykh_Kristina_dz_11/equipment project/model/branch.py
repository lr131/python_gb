from equipment import Equipment


class Branch:
    """Подразделение компании"""
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def take(self, equipment):
        pass
