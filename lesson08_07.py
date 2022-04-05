class Complex:
    def __init__(self, complex):
        self.complex = complex


    def __add__(self, other):
        return Complex([self.complex[i] + other.complex[i] for i in range(len(self.complex))])


    def __mul__(self, other):
        return Complex([self.complex[0] * other.complex[0] - self.complex[1] * other.complex[1], self.complex[0] * other.complex[1] + self.complex[1] * other.complex[0]])


    def __str__(self):
        return f'{self.complex[0]} + {self.complex[1]}i'


complex1 = []
complex2 = []
print(f'арифметические действия с комплексными числами вида a + bi:')
try:
    complex1.append(float(input('"a" первого комплексного числа: ')))
    complex1.append(float(input('"b" первого комплексного числа: ')))
    complex2.append(float(input('"a" второго комплексного числа: ')))
    complex2.append(float(input('"b" второго комплексного числа: ')))
except (ValueError, TypeError, NameError):
    print('ошибка ввода')
cp1 = Complex(complex1)
cp2 = Complex(complex2)

print('результат сложения комплексных чисел: ', cp1 + cp2)
print('результат умножения комплексных чисел: ', cp1 * cp2)