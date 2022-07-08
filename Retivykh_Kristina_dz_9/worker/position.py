from worker.worker import Worker


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        """Возвращает полное имя сотрудника"""

        return f'{self.name} {self.surname}'

    def get_total_income(self):
        """Возвращает полный доход"""
        return self._income["wage"] + self._income["bonus"]
