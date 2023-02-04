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
from math import log10, floor


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


def revers_5(enter_num):
    return ''.join(reversed(str(enter_num).strip()))


def revers_6(enter_num):
    if enter_num < 10:
        return enter_num
    num_length = floor(log10(enter_num))
    res = 0
    for k in range(1, num_length + 1):
        res += floor(enter_num * 10 ** (-k)) * 10**(num_length - k)
    res = enter_num * 10 ** num_length - 99 * res
    return res


if __name__ == "__main__":
    nums = [randint(10000, 1000000), randint(1000000, 10000000), randint(100000000, 10000000000000)]
    n_tests = 1000000
    texts = ["Рекурсия", "While", "Преобразование в str и срез", "f строка и срез", "Переворот списка", "По формуле"]
    funcs = ['revers', 'revers_2', 'revers_3', 'revers_4', 'revers_5', 'revers_6']

    for i, f in enumerate(funcs):
        print(texts[i])
        for j in range(len(nums)):
            fu = f'{f}(nums[{j}])'
            print(timeit(fu, globals=globals(), number=n_tests))
        print()

"""
Рекурсия ничего не возвращала

Рекурсия
2.1458342999999998
2.4233274000000002
4.962596400000001

While
1.5521004999999999
1.7827906999999996
3.3872243000000015

Преобразование в str и срез
0.5040234999999988
0.5089964999999985
0.5679547000000014

f строка и срез
0.39686280000000096
0.36157869999999903
0.4119289999999971

Переворот списка
1.1183591000000028
1.1299770000000002
1.3682447999999994

По формуле
4.6065079
6.006021800000003
12.709115400000002

Вариант с f строкой самый быстрый, самый читаемый, занимает 1 строку кода
"""
