"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""
from timeit import timeit


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    dct = {}
    m = 0
    el = None
    for x in array:
        dct[x] = 1 + dct.setdefault(x, 0)
        if m < dct[x]:
            m = dct[x]
            el = x
    return f'Чаще всего встречается число {el}, ' \
           f'оно появилось в массиве {m} раз(а)'


if __name__ == "__main__":
    array = [2, 1, 3, 1, 3, 4, 5, 1, 0, 10]
    #array = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    #array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(func_1())
    print(func_2())
    print(func_3())
    n_tests = 1000000
    texts = ["count", "count+max", "dict"]
    funcs = ['func_1', 'func_2', 'func_3']
    for i, f in enumerate(funcs):
        print(texts[i])
        fu = f'{f}()'
        se = f'from __main__ import {f}'
        print(timeit(fu, setup=se, number=n_tests))

"""
В общем случае 
[2, 1, 3, 1, 3, 4, 5, 1, 0, 10]
словарь немного выигрывает:
count
3.0550787
count+max
4.006722699999999
dict
2.9706026999999997

Если все элементы одинаковые
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
первый вариант сильно быстрее
count
1.8498089
count+max
2.8397445
dict
3.1815127

Если все элементы разные
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
словарь еще чуть быстрее
count
3.0779209
count+max
3.9878544000000002
dict
2.8081332000000003
"""
