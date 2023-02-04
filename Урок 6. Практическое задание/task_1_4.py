"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python

На каждый скрипт нужно два решения - исходное и оптимизированное.

Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler

Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler

Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.


ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.

Это файл для четвертого скрипта


ДЗ 1 из курса основ, задача 2


Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень
числа X):
a. Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 –
делится нацело на 7. Внимание: использовать только арифметические операции!
b. К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого
списка, сумма цифр которых делится нацело на 7.
c. * Решить задачу под пунктом b, не создавая новый список.

"""
from numpy import array
from memory_profiler import profile


def sum_list_1(dataset: list) -> int:
    """Вычисляет сумму чисел списка dataset, сумма цифр которых делится нацело на 7"""
    # место для написания кода
    summ = 0
    for numb in dataset:
        sum_dig = sum_of_digits(numb)
        if (sum_dig % 7) == 0:
            summ += numb
    return summ  # Верните значение полученной суммы


# def sum_list_2(dataset: list) -> int:
#     """К каждому элементу списка добавляет 17 и вычисляет сумму чисел списка,
#         сумма цифр которых делится нацело на 7"""
#     # место для написания кода
#     summ = 0
#     for numb in dataset:
#         sum_dig = sum_of_digits(numb + 17)
#         if (sum_dig % 7) == 0:
#             summ += numb + 17
#     return summ  # Верните значение полученной суммы


def sum_of_digits(numb: int):
    summ = 0
    while numb > 0:
        summ += numb % 10
        numb = numb // 10
    return summ


@profile
def fill_list_lc():
    my_list = [i ** 3 for i in range(3, 100000, 2)]  # Соберите нужный список по заданию
    print(sum_list_1(my_list))


@profile
def fill_numpy_array():
    my_list = array([n ** 3 for n in range(3, 100000, 2)])
    print(sum_list_1(my_list))
    print(sum_list_1(my_list))


if __name__ == '__main__':
    fill_list_lc()
    fill_numpy_array()


"""
1409831608061185538


Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    68     30.7 MiB     30.7 MiB           1   @profile
    69                                         def fill_list_lc():
    70     33.2 MiB      2.5 MiB       50002       my_list = [i ** 3 for i in range(3, 100000, 2)]  # Соберите нужный список по заданию
    71     33.2 MiB      0.0 MiB           1       print(sum_list_1(my_list))


1409831608061185538

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    74     31.2 MiB     31.2 MiB           1   @profile
    75                                         def fill_numpy_array():
    76     33.2 MiB      0.6 MiB       50002       my_list = array([n ** 3 for n in range(3, 100000, 2)])
    77     31.8 MiB     -1.4 MiB           1       print(sum_list_1(my_list))


NumPy позволяет экономить память

"""