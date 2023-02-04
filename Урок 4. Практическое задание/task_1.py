"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""
from timeit import Timer


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i, x in enumerate(nums) if x % 2 == 0]


if __name__ == "__main__":
    a = [x for x in range(10000)]
    t1 = Timer("func_1(a)", "from __main__ import func_1, a")
    print(f'Append {t1.timeit(number=100000)} sec')
    t2 = Timer("func_2(a)", "from __main__ import func_2, a")
    print(f'LC {t1.timeit(number=100000)} sec')

"""
Append 118.6185954 sec
LC 117.7041988 sec

Читаемость кода улучшилась, время почти не изменилось

"""
