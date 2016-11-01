#!/usr/bin/python
# coding=UTF-8
__author__ = 'fdts'

print("Hallo world")

etot = 'Этот'
var = 'вариант'
print('1. На %s variant' % etot)
print(etot + ' вариант тоже можно использовать, но не рекомендуется')
print('3. Или на %s %s' % (etot, var))
print('4. Или на %(etot)s %(var)s' % {'etot': etot, 'var': var})  # Очень удобно для локализаторов (создаеться словарь)
print('5. Или на {} {}'.format(etot, var))
print('6. Или на {1} {0}'.format(var, etot))
print('7. Или на {etot} {var}'.format(var=var, etot=etot))

#обьявление кортежа
tn = 2,54,7,5,85
print(tn)

#обьявление словаря
slovar = {"name":"Буруедук", "version":"138.25.8", "Category":"5"}
print(slovar)
print(slovar["name"])
slovar["name"] = "Солнце" #оператор присвоения
print(slovar["name"])

#ссылки
list1 = [5,8,9] #создание списка
print('list1 = ', list1)
list2 = list1 #список 12 получает ссылку на список 11, копия списка не создаеться !
list2[0] = 258
print(list1)

#логические величины
log1 = True
log2 = False
print(log1, log2)
x= 10
y = 28
print(x == y)
print(x < y)
log1 = x > y
print("log1 =",log1)
#сравнение строк
s1 = "Python"
s2 = "Django"
log2 = s1 != s2
print("log2 =", log2)
#сравнение списков
list2 = [7,8,6,3]
print(list2)
x = 8
log1 = x in list2 #наличие значение элемента x в списке
print("Входит ли значение %s в список list2 (%s) ?" % (x,list2), log1)
log2 = list1 == list2
print("Сравнение двух "
      "списков list1(%s) и list2(%s) происходит по элементно -" % (list1,list2),log2 )
list3 = [7,8]
log1 = list3 == list2
print("Сравнение двух "
      "списков list3(%s) и list2(%s) происходит по элементно, при равно элементы НЕ игнорирюються" % (list3, list2), log1 )
del list3
list3 = [5,6]
log1 = list2 > list3
print("Сравнение двух "
      "списков list2(%s) > list3(%s) происходит по элементно, лишние элементы игнориються -" % (list2, list3), log1 )

#преобразование типов
s = "Django"
if 2 < 3 and s:
    n=101
else:
    n=2
print(n)

#Условное выражение
z = 100
if x > y:
    n=201
elif x == y: #если здесь поставить > то выдасться значение n = 301, остольные elif будут проинорированы
    n = 301
elif z > y:
    n = 401 #выдаст это значение
else:
    n = 501
print("Значения x,y,z и n соответственно",x,y,z,n)

#Циклы
n = 0
x = 0
while n <= 6:
    x = x + 1
    print(x)
    n = n + 1

ls = [2,8,32,129]
ld = []
for el in ls:
    ld = ld + [2**el] #происходит заполнение списка
print(ld)
#прерывание цикла
ld = []
for el in ls:
    if el > 100:
        break
    ld = ld + [2 ** el]
print(ld)
#пропуск шага цикла
ld = []
for el in ls:
    if el < 100:
        continue
    ld = ld + [2 ** el]
print(ld)
