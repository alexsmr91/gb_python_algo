"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""
from timeit import timeit
from random import randint


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num // 10
    else:
        num = enter_num % 10
        revers_num = (revers_num + num) * 10
        enter_num //= 10
        return revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return int(revers_num)


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    return f'{enter_num}'[::-1]


if __name__ == "__main__":
    nums = [randint(10000, 1000000), randint(1000000, 10000000), randint(100000000, 10000000000000)]
    n_tests = 1000000
    texts = ["Рекурсия", "While", "Преобразование в str и срез", "f строка и срез"]
    funcs = ['revers', 'revers_2', 'revers_3', 'revers_4']

    for i, f in enumerate(funcs):
        print(texts[i])
        for j in range(len(nums)):
            fu = f'{f}(nums[{j}])'
            se = f'from __main__ import {f}, nums'
            print(timeit(fu, setup=se, number=n_tests))
        print()

"""
Рекурсия ничего не возвращала

Рекурсия
2.0632390000000003
2.2919603
4.4018714999999995

While
1.4254774000000001
1.5940426999999993
2.9253131999999997

Преобразование в str и срез
0.46702279999999874
0.48050709999999874
0.49645079999999986

f строка и срез
0.3458843000000016
0.3538274000000001
0.3945564000000026

Последний вариант с f строкой самый быстрый, самый читаемый, занимает 1 строку кода
"""
