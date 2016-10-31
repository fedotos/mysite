#!/usr/bin/python
# coding=UTF-8
__author__ = 'fdts'

print("Hallo world")


etot = 'Этот'
var = 'вариант'
print('1. На %s variant' % etot)
print(etot + ' вариант тоже можно использовать, но не рекомендуется')
print('3. Или на %s %s' % (etot, var))
print('4. Или на %(etot)s %(var)s' % {'etot': etot, 'var': var})  # Очень удобно для локализаторов
print('5. Или на {} {}'.format(etot, var))
print('6. Или на {1} {0}'.format(var, etot))
print('7. Или на {etot} {var}'.format(var=var, etot=etot))