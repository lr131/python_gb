from decimal import DivisionByZero


class MyDivisionByZero(Exception):
    def __init__(self, *args):
        if args:
            self.message=args[0]
        else:
            self.message=None
            
    def __str__(self):
        if self.message:
            return f"MyDivisionByZero {self.message}"
        else:
            return "MyDivisionByZero has been raised"


class MyNumber(int):
    
    def __init__(self, num):
        self.__num = num
        
    def __str__(self):
        return str(self.__num)
        
    def __truediv__(self, obj):
        if obj.__num == 0:
            raise MyDivisionByZero
        else:
            return MyNumber(self.__num / obj.__num)
            

if __name__ == '__main__':
    mn1 = MyNumber(5)
    mn2 = MyNumber(0)
    mn3 = MyNumber(2)
    try:
        print(mn1 / mn2)
    except MyDivisionByZero as e:
        print(e)
    print(mn1 / mn3)