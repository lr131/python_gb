class OutOfStoreError(BaseException):
    def __init__(self, *args):
        if args:
            self.message=args[0]
        else:
            self.message=None
            
    def __str__(self):
        if self.message:
            return f"OutOfStoreError {self.message}"
        else:
            return "Невозможно доставить оборудование: на складе нет места"
        
class NotFoundEquipmentError(BaseException):
    def __init__(self, *args):
        if args:
            self.message=args[0]
        else:
            self.message=None
            
    def __str__(self):
        if self.message:
            return f"NotFoundEquipmentError {self.message}"
        else:
            return "Запрашиваемое оборудование не найдено"
        
class LogisticPathEquipmentError(BaseException):
    def __init__(self, *args):
        if args:
            self.message=args[0]
        else:
            self.message=None
            
    def __str__(self):
        if self.message:
            return f"LogisticPathEquipmentError {self.message}"
        else:
            return "На запрашиваемое оборудование отсутствуют документы"