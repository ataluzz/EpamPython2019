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

#task2

class Quaternion:
    
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        
    def __eq__(self, other):
        return self.a == other.a and \
           self.b == other.b and \
           self.c == other.c and \
           self.d == other.d
    
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
    
    @classmethod
    def inversed(cls):
        sq = self.a**2 + self.b**2 + self.c**2 + self.d**2
        return cls(self.a / sq, self.b / sq, self.c / sq, self.d / sq)
    
    def __truediv__(self, other):
        """This method returns left quotient.
        For getting right quotient use q2.right_quotient(q3)"""
        left_quotient = self.inversed() * other
        return left_quotient
        
    def right_quotient(self, other):
        """This method returns right quotient.
        For getting left quotient use q2 / q3"""
        right_quotient = other * self.inversed()
        return right_quotient
