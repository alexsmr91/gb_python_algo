"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from collections import OrderedDict
from random import randint
from timeit import timeit


def fill_dict(num: int, limit: int):
    dct = {}
    for i in range(num):
        dct.setdefault(i, randint(-limit, limit))
    return dct


def fill_odict(num: int, limit: int):
    odct = OrderedDict()
    for i in range(num):
        odct.setdefault(i, randint(-limit, limit))
    return odct


def edit_dict(dct: dict, limit: int):
    for key in dct.keys():
        dct[key] = randint(-limit, limit)


def edit_odict(odct: OrderedDict, limit: int):
    for key in odct.keys():
        odct[key] = randint(-limit, limit)


def pop_dict(dct: dict):
    for i in range(len(dct)):
        dct.popitem()


def pop_odict(odct: OrderedDict):
    for i in range(len(odct)):
        odct.popitem()


def rnd_access_dict(dct: dict, num: int):
    keys = list(dct.keys())
    for i in range(num):
        a = dct[keys[randint(0, len(dct) - 1)]]


def rnd_access_odict(odct: OrderedDict, num: int):
    keys = list(odct.keys())
    for i in range(num):
        a = odct[keys[randint(0, len(odct) - 1)]]


if __name__ == "__main__":
    n_elements = 10000000
    n_tests = 1
    lim = 100000

    print(f'Fill dict {timeit("fill_dict(n_elements, lim)", globals=globals(), number=n_tests)} sec')
    print(f'Fill o-dict {timeit("fill_odict(n_elements, lim)", globals=globals(), number=n_tests)} sec')

    dct = fill_dict(n_elements, lim)
    odct = fill_odict(n_elements, lim)

    print(f'Edit dict {timeit("edit_dict(dct, lim)", globals=globals(), number=n_tests)} sec')
    print(f'Edit o-dict {timeit("edit_odict(odct, lim)", globals=globals(), number=n_tests)} sec')

    print(f'Rnd access dict {timeit("rnd_access_dict(dct, n_elements * 10)", globals=globals(), number=n_tests)} sec')
    print(f'Rnd access o-dict '
          f'{timeit("rnd_access_odict(odct, n_elements * 10)", globals=globals(), number=n_tests)} sec')

    print(f'Pop dict {timeit("pop_dict(dct)", globals=globals(), number=n_tests)} sec')
    print(f'Pop o-dict {timeit("pop_odict(odct)", globals=globals(), number=n_tests)} sec')


"""
Заполнение обычных словарей на ~10% быстрее 

Fill dict 17.3881475 sec
Fill o-dict 19.2977578 sec

Изменение значений происходит примерно за одно и тоже время

Edit dict 15.711223000000004 sec
Edit o-dict 15.590509699999998 sec

Случайный доступ выполняется за одно и то же время

Rnd access dict 208.9088327 sec
Rnd access o-dict 210.37171990000002 sec

Удаление пар происходит быстрее у обычных словарей

Pop dict 1.2337976000000026 sec
Pop o-dict 2.2716667000000115 sec


o-dict можно использовать, если нужны спецефичные методы:
move_to_end(key, last=True), popitem(last=True)
"""
