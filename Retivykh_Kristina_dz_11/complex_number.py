class ComplexNumber:
    
    def __init__(self, real, imaginary):
        if isinstance(real, int | float):
            self.real = real
        elif isinstance(real, str) and (real.isdigit):
            self.real = float(real)
        else:
            raise TypeError
        if isinstance(imaginary, int | float):
            self.imaginary = imaginary
        elif isinstance(imaginary, str) and (imaginary.isdigit):
            self.imaginary = float(imaginary)
        else:
            raise TypeError
        
    def __add__(self, obj):
        return ComplexNumber(self.real + obj.real, self.imaginary + obj.imaginary)
    
    def __sub__(self, obj):
        return ComplexNumber(self.real - obj.real, self.imaginary - obj.imaginary)
        

    def __mul__(self, obj):
        return ComplexNumber(self.real * obj.real - (self.imaginary * obj.imaginary), self.imaginary * obj.real)

    def __eq__(self, other):
        return (self.real == other.real) and (self.imaginary == other.imaginary)
    
    def __str__(self):
        return f'({self.real} + {self.imaginary}*i)'
    
    
if __name__ == '__main__':
    z1 = ComplexNumber(5, -6)
    z2 = ComplexNumber(-3, 2)

    
    print("печатаем комплексное число: ", z1)
    print(f"сумма: {z1} + {z2} = ", z1 + z2)
    print(f"разность: {z1} - {z2} = ", z1 - z2)
    print(f"умножение: {z1} * {z2} = ", z1 * z2)
    
    z3 = ComplexNumber('5.2', 4)
    print("Ввод float через str:", z3)
