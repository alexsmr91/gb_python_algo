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


def func_4():
    el = max(array, key=array.count)
    return f'Чаще всего встречается число {el}, ' \
           f'оно появилось в массиве {array.count(el)} раз(а)'


if __name__ == "__main__":
    array = [2, 1, 3, 1, 3, 4, 5, 1, 0, 10]
    #array = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    #array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n_tests = 1000000
    texts = ["count", "count+max", "dict", "1 line"]
    funcs = ['func_1', 'func_2', 'func_3', 'func_3']
    for i, f in enumerate(funcs):
        print(texts[i])
        fu = f'{f}()'
        print(timeit(fu, globals=globals(), number=n_tests))

"""
В общем случае 
[2, 1, 3, 1, 3, 4, 5, 1, 0, 10]
Решение в 1 строку немного выигрывает:

count
3.1953207999999997
count+max
4.1310044
dict
3.0941378000000004
1 line
3.0227658


Если все элементы одинаковые
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
первый вариант сильно быстрее

count
1.7413644
count+max
2.7206059999999996
dict
3.2644982000000002
1 line
3.2797252000000006


Если все элементы разные
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Решение в 1 строку еще чуть быстрее

count
3.4294857000000003
count+max
4.4816308
dict
3.0715350999999993
1 line
2.8924874000000003
"""
