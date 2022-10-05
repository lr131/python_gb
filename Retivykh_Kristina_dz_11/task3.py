# 3. Создайте собственный класс-исключение, 
# который должен проверять содержимое списка 
# на наличие только чисел. Проверить работу исключения на реальном примере. 
# Запрашивать у пользователя данные и заполнять список необходимо только числами. 
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. 
# Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду «stop». 
# При этом скрипт завершается, сформированный список с числами выводится на экран.
# Подсказка: для этого задания примем, что пользователь может вводить только числа и строки. 
# Во время ввода пользователем очередного элемента необходимо реализовать проверку типа элемента. 
# Вносить его в список, только если введено число. Класс-исключение должен 
# не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение. 
# При этом работа скрипта не должна завершаться.
from pprint import pprint

class NumberError(ValueError):
    def __init__(self, *args):
        if args:
            self.message=args[0]
        else:
            self.message=None
            
    def __str__(self):
        if self.message:
            return f"NumberError {self.message}"
        else:
            return "NumberError has been raised"


class MyNumber:
    def __init__(self, value):
        if isinstance(value, int):
            self.value = value
        elif value.isdigit():
            self.value = int(value)
        else:
            raise NumberError
    
    def __str__(self) -> str:
        return f"{self.value}"
    
    def to_int(self):
        return self.value

if __name__ == '__main__':
    print("Введите числа через enter")
    data = []
    
    while True:
        try:
            val = input()
            if val.lower() == 'stop':
                break
            MyNumber(val)
            data.append(int(val))
        except NumberError as e:
            print(e)
            continue
    
    print(data)
