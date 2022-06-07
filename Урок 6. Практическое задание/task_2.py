"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение


Урок 4 по алгоритмам, задание 3.


Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.
Сделайте профилировку каждого алгоритма через timeit
Обязательно предложите еще свой вариант решения!
Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""
from random import randint
from memory_profiler import profile


@profile
def wrapped_revers(num: int):
    def revers(enter_num, revers_num=0):
        if enter_num == 0:
            return revers_num // 10
        else:
            num = enter_num % 10
            revers_num = (revers_num + num) * 10
            enter_num //= 10
            return revers(enter_num, revers_num)
    return revers(num)


if __name__ == "__main__":
    a = randint(999999999, 9999999999)
    print(a, '-', wrapped_revers(a))


"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    24     19.0 MiB     19.0 MiB           1   @profile
    25                                         def wrapped_revers(num: int):
    26     19.0 MiB      0.0 MiB          12       def revers(enter_num, revers_num=0):
    27     19.0 MiB      0.0 MiB          11           if enter_num == 0:
    28     19.0 MiB      0.0 MiB           1               return revers_num // 10
    29                                                 else:
    30     19.0 MiB      0.0 MiB          10               num = enter_num % 10
    31     19.0 MiB      0.0 MiB          10               revers_num = (revers_num + num) * 10
    32     19.0 MiB      0.0 MiB          10               enter_num //= 10
    33     19.0 MiB      0.0 MiB          10               return revers(enter_num, revers_num)
    34     19.0 MiB      0.0 MiB           1       return revers(num)


8968375695 - 5965738698

Чтобы не было кучи таблиц с замерами нужно обернуть функцию

"""
