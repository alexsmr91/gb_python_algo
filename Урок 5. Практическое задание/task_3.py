"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее

2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее

3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее

Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах. Для замеров используйте timeit.
"""
from collections import deque
from random import randint
from timeit import timeit


def lst_append(num: int, limit: int):
    ls = list()
    for i in range(num):
        ls.append(randint(-limit, limit))
    return ls


def deq_append(num: int, limit: int):
    dq = deque()
    for i in range(num):
        dq.append(randint(-limit, limit))
    return dq


def lst_pop(ls: list):
    for i in range(len(ls)):
        ls.pop()


def deq_pop(dq: deque):
    for i in range(len(dq)):
        dq.pop()


def lst_ext(ls1: list, ls2: list):
    ls1.extend(ls2)


def deq_ext(dq1: deque, dq2: deque):
    dq1.extend(dq2)


def lst_append_left(num: int, limit: int):
    ls = list()
    for i in range(num):
        ls.insert(0, randint(-limit, limit))
    return ls


def deq_append_left(num: int, limit: int):
    dq = deque()
    for i in range(num):
        dq.appendleft(randint(-limit, limit))
    return dq


def lst_pop_left(ls: list):
    for i in range(len(ls)):
        ls.pop(0)


def deq_pop_left(dq: deque):
    for i in range(len(dq)):
        dq.popleft()


def lst_ext_left(ls: list, ls1: list):
    for el in ls1:
        ls.insert(0, el)
    return ls


def deq_ext_left(dq: deque, dq1: deque):
    return dq.extendleft(dq1)


def lst_rnd_access(ls: list, num: int):
    length = len(ls)
    for i in range(num):
        a = ls[randint(0, length - 1)]


def deq_rnd_access(dq: deque, num: int):
    length = len(dq)
    for i in range(num):
        a = dq[randint(0, length - 1)]


if __name__ == "__main__":
    n_elements = 1000000
    n_tests = 1
    lim = 100000

    print(f'List append {timeit("lst_append(n_elements, lim)", globals=globals(), number=n_tests)} sec')
    print(f'Deque append {timeit("deq_append(n_elements, lim)", globals=globals(), number=n_tests)} sec')
    lst = lst_append(n_elements, lim)
    deq = deq_append(n_elements, lim)

    print(f'List pop {timeit("lst_pop(lst)", globals=globals(), number=n_tests)} sec')
    print(f'Deque pop {timeit("deq_pop(deq)", globals=globals(), number=n_tests)} sec')

    lst = lst_append(n_elements, lim)
    deq = deq_append(n_elements, lim)
    lst1 = lst_append(n_elements, lim)
    deq1 = deq_append(n_elements, lim)

    tst_time = timeit("lst_ext(lst, lst1)", globals=globals(), number=n_tests)
    print(f'List extend {tst_time} sec')

    tst_time = timeit("deq_ext(deq, deq1)", globals=globals(), number=n_tests)
    print(f'Deque extend {tst_time} sec')

    tst_time = timeit("lst_append_left(n_elements, lim)", globals=globals(), number=n_tests)
    print(f'List append left {tst_time} sec')

    tst_time = timeit("deq_append_left(n_elements, lim)", globals=globals(), number=n_tests)
    print(f'Deque append left {tst_time} sec')

    lst = lst_append(n_elements, lim)
    deq = deq_append(n_elements, lim)

    tst_time = timeit("lst_pop_left(lst)", globals=globals(), number=n_tests)
    print(f'List pop left {tst_time} sec')

    tst_time = timeit("deq_pop_left(deq)", globals=globals(), number=n_tests)
    print(f'Deque pop left {tst_time} sec')

    lst = lst_append(n_elements, lim)
    deq = deq_append(n_elements, lim)
    lst1 = lst_append(n_elements, lim)
    deq1 = deq_append(n_elements, lim)

    tst_time = timeit("lst_ext_left(lst, lst1)", globals=globals(), number=n_tests)
    print(f'List extend left {tst_time} sec')

    tst_time = timeit("deq_ext_left(deq, deq1)", globals=globals(), number=n_tests)
    print(f'Deque extend left {tst_time} sec')

    lst = lst_append(n_elements, lim)
    deq = deq_append(n_elements, lim)

    print(f'List random access '
          f'{timeit("lst_rnd_access(lst, n_elements * 10)", globals=globals(), number=n_tests)} sec')
    print(f'Deque random access '
          f'{timeit("deq_rnd_access(deq, n_elements * 10)", globals=globals(), number=n_tests)} sec')


"""
1)Операции append, pop, extend выполняются за одно и тоже время у list и deque

List append 15.940860300000002 sec
Deque append 16.999495399999997 sec
List pop 0.8327705000000023 sec
Deque pop 0.8098118000000056 sec
List extend 0.1809119999999922 sec
Deque extend 0.18158780000000263 sec


2)Добавление, удаление и объединение слева на deque работает в разы быстрее, чем на list

List append left 37.810379999999997 sec
Deque append left 1.5394880000000022 sec
List pop left 65.138985 sec
Deque pop left 0.09230399999999861 sec
List extend left 97.31318500000002 sec
Deque extend left 0.012663000000010527 sec


3)Случайный доступ к элементам быстрее у list

List random access 16.141307 sec
Deque random access 42.841989 sec
"""
