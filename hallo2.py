#!/usr/bin/python
# coding=UTF-8
__author__ = 'fdts'
from fractions import Fraction #импорт клааса Fraction из модуля fractions

print("Hallo world 2 !")

f = Fraction(8,6) #создаем новый экземпляр оъекта fraction
a = f.numerator
b = f.denominator
x = 111
print(a,b)

f1 = Fraction.from_float(3.5)
print(f1)

#объявление классов - Родитель 1
class Square:
    a = 0
    b = 0
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def area(self):
        return self.a * self.b
    @staticmethod #не принимает ссылку на самого себя, при вызове нужно указать занчения a и b
    def get_area(a,b):
        return a * b
    def pereop(self):
        return self.a + self.b
sq = Square(55,2)
print(sq.area())
print(sq.get_area(2,3))
print("pereop (a = %s, b = %s) = %s" % (sq.a,sq.b,sq.pereop()))

#наследование - Родитель 2
class Cube(Square):
    z = 0
    def __init__(self,a,b,z):
        Square.__init__(self,a,b)
        self.z = z
    def area(self):
        return super(Cube, self).area() + 1
    def volume(self):
        return Square.area(self) * self.z


cub = Cube(2,3,10)
print(cub.a,cub.b,cub.z)
print(cub.volume())

#наследование родит1 -- родит2 -- дочерн
class Morecub(Cube):
    t = 0
    def __init__(self,a,b,z,t):
        Cube.__init__(self,a,b,z)
        self.t = t
    def area(self):
        x = super(Morecub, self).area()
        return x * self.t
    def pereop(self): #переопределим метод родителя 1 (не зная его имени)
        return super(Morecub, self).pereop() - 20
cubm = Morecub(2,3,4,5)
print("Morecub.area =", cubm.area())
print("(a = %s, b = %s) Morecub.pereop =", cubm.pereop())
