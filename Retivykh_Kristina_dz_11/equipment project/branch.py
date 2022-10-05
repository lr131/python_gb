class Branch:
    """Подразделение компании"""
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.store = []

    def remove(self, equipment):
        return self.store.pop(equipment)
    
    def add(self, equipment):
        self.store.append(equipment)
        
    def __str__(self):
        return (f"Подразделение {self.name}\n"
                f"Расположение {self.location}\n"
                f"Оборудование: {tuple(map(lambda x: x.to_dict(), self.store))} ")
