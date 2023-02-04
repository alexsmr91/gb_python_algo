"""
Задание 1.

Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100]. Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в виде функции.

Обязательно доработайте алгоритм (сделайте его умнее)!

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.

Обязательно сделайте замеры времени обеих реализаций и дайте ответ помогла ли
доработка и в каких случаях она будет эффективной.

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.
"""
from random import randint
from timeit import timeit


def bubble_desc_smart(array: list):
    i = 0
    n = len(array)
    fl = True
    while (i < len(array) - 1) and fl:
        j = 0
        fl = False
        while j < n - 1 - i:
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                fl = True
            j += 1
        i += 1
    return array


def bubble_desc(array: list):
    i = 0
    n = len(array)
    while i < len(array) - 1:
        j = 0
        while j < n - 1 - i:
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
            j += 1
        i += 1
    return array


if __name__ == "__main__":
    n_tests = 100
    lst = [randint(-100, 100) for _ in range(500)]
    #lst = [x for x in range(-250, 250)]
    #lst = [x for x in range(250, -250, -1)]
    print(lst)
    print(bubble_desc(lst[:]))
    print(bubble_desc_smart(lst[:]))
    print(f'Обычный пузырёк {timeit("bubble_desc(lst[:])", globals=globals(), number=n_tests)} sec')
    print(f'Умный пузырёк {timeit("bubble_desc_smart(lst[:])", globals=globals(), number=n_tests)} sec')

"""
умный пузырёк дает выйгрыш по времени, особенно если массив уже отсортирован

На входе уже отсортированный массив:
Обычный пузырёк 2.52542 sec
Умный пузырёк 0.01202930000000002 sec

На входе отсортированный в другую сторону массив:
Обычный пузырёк 4.6307694 sec
Умный пузырёк 4.4895324 sec


На входе случайный массив:
Обычный пузырёк 3.6307122 sec
Умный пузырёк 3.5833331999999998 sec
"""
