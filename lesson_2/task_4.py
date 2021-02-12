"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def f_sum(n, summ=1, a=1):
    if n < 2:
        return summ
    else:
        a = a / -2
        return f_sum(n - 1, summ + a, a)


n1 = None
while type(n1) is not int:
    try:
        n1 = int(input('Введите число элементов для ряда чисел: '))
    except ValueError:
        print('ошибка ввода')

print(f_sum(n1))
