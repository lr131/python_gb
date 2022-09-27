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

    def __mul__(self, obj):
        return ComplexNumber(self.real * obj.real - (self.imaginary * obj.imaginary), self.imaginary * obj.real)

    def __str__(self):
        return f'z = {self.real} + {self.imaginary}*i'
    
    
if __name__ == '__main__':
    z1 = ComplexNumber(1, 3)
    z2 = ComplexNumber(7, 2)
    
    print(z1)
    print(z1 + z2)
    print(z1 * z2)
    
    z3 = ComplexNumber('5.2', 4)
    print(z3)
