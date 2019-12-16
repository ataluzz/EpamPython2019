"""
Реализовать класс Quaternion, позволяющий работать с кватернионами
https://ru.wikipedia.org/wiki/%D0%9A%D0%B2%D0%B0%D1%82%D0%B5%D1%80%D0%BD%D0%B8%D0%BE%D0%BD
Функциональность (магическими методами):
- сложение
- умножение
- деление
- сравнение
- нахождение модуля
- строковое представление и repr
По желанию:
- взаимодействие с числами других типов
"""

class Quaternion:
    
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        
    def __eq__(self, other):
        return self.__abs__ == other.__abs__
    
    def __str__(self):
        return f"{self.a} {self.b}i {self.c}j {self.d}k"
    
    def __repr__(self):
        return f"Quaternion({self.a}, {self.b}, {self.c}, {self.d})"
    
    def __add__(self, other):
        return Quaternion(self.a + other.a, self.b + other.b, self.c + other.c, self.d + other.d)
           
    def __mul__(self, other):
        a = self.a*other.a - self.b*other.b - self.c*other.c - self.d*other.d
        b = self.a*other.b + self.b*other.a + self.c*other.d - self.d*other.c
        c = self.a*other.c + self.c*other.a + self.d*other.b - self.b*other.d
        d = self.a*other.d + self.d*other.a + self.b*other.c - self.c*other.b
        return Quaternion(a, b, c, d)
    
    def __abs__(self):
        return (self.a**2 + self.b**2 + self.c**2 + self.d**2)**0.5
    
    def inversed(self):
        sq = self.a**2 + self.b**2 + self.c**2 + self.d**2
        return Quaternion(self.a / sq, self.b / sq, self.c / sq, self.d / sq)
    
    def __truediv__(self, other):
        left_quotient = self * other.inversed()
        right_quotient = other * self.inversed()
        return left_quotient, right_quotient
