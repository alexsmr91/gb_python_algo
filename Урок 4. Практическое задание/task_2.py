"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию
Выполнена попытка оптимизировать решение мемоизацией
Сделаны замеры обеих реализаций.

Сделайте аналитику, нужна ли здесь мемоизация или нет и почему?!!!

П.С. задание не такое простое, как кажется
"""

from timeit import timeit
from random import randint


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


def memoize(f):
    cache = {}

    def decorate(*args):

        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorate


@memoize
def recursive_reverse_mem(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


if __name__ == "__main__":
    num_100 = randint(10000, 1000000)
    num_1000 = randint(1000000, 10000000)
    num_10000 = randint(100000000, 10000000000000)

    n_tests = 1000000

    print('Не оптимизированная функция recursive_reverse')
    print(timeit("recursive_reverse(num_100)", globals=globals(), number=n_tests))
    print(timeit("recursive_reverse(num_1000)", globals=globals(), number=n_tests))
    print(timeit("recursive_reverse(num_10000)", globals=globals(), number=n_tests))

    print('Оптимизированная функция recursive_reverse_mem')
    print(timeit('recursive_reverse_mem(num_100)', globals=globals(), number=n_tests))
    print(timeit('recursive_reverse_mem(num_1000)', globals=globals(), number=n_tests))
    print(timeit('recursive_reverse_mem(num_10000)', globals=globals(), number=n_tests))

"""
Благодаря декоратору кэширования вычисления производятся только в первом прогоне теста,
остальные прогоны не вычисляются, а берутся из кэша

Не оптимизированная функция recursive_reverse
3.4795785
3.8612288
7.2221372
Оптимизированная функция recursive_reverse_mem
0.2264122000000004
0.2497480000000003
0.27421960000000034
"""
