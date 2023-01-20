def func(x, y):
    z = f'Сумма чисел равна: {x + y}'
    c = f'Разность чисел равна: {x - y}'
    try:
        n =f'Частное чисел равняется: {x / y}'
    except ZeroDivisionError as p:
        n = p
    m = f'Произведение чисел равняется: {x * y}'
    return z, c, n, m


try:
    x = int(input('Введите первое число: '))
    y = int(input('Введите второе число: '))
except:
    print('Вы ввели не числовое значение')
else:
    z, c, n, m = func(x, y)
    print(z)
    print(c)
    print(n)
    print(m)