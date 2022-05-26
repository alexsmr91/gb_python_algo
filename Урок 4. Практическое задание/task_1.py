"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""
from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i, x in enumerate(nums) if x % 2 == 0]


if __name__ == "__main__":
    n_tests = 1000000
    a = [x for x in range(10000)]
    print(f'Append {timeit("func_1(a)", globals=globals(), number=n_tests)} sec')
    print(f'LC {timeit("func_2(a)", globals=globals(), number=n_tests)} sec')

"""
Append 120.91151649999999 sec
LC 95.49185170000001 sec

Читаемость кода улучшилась, LC быстрее на 15-20%

"""
