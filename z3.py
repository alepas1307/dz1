# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

x = float(input('Введите координату X: '))
while x == 0:
    print ('Х не может равняться нулю.') 
    x = float(input('Введите координату X: '))
y = float(input('Введите координату Y: '))
while y == 0:
    print ('Y не может равняться нулю.') 
    y = float(input('Введите координату Y: '))
if x > 0 and y > 0:
    print ('Точка находится в I четверти.')
if x < 0 and y > 0:
    print ('Точка находится во II четверти.')
if x < 0 and y < 0:
    print ('Точка находится в III четверти.') 
if x > 0 and y < 0:
    print ('Точка находится в IV четверти.') 