"""
Задание 2.	Подсчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной.
При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены, рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.

Решите через рекурсию. В задании нельзя применять циклы.

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""


def digits(num: int):
    if num == 0:
        return 0, 0
    odd = 0
    even = 0
    last = num % 10
    head = num // 10
    if last % 2 == 1:
        odd = 1
    elif last != 0:
        even = 1
    sub_res = digits(head)
    return sub_res[0] + even, sub_res[1] + odd


if __name__ == "__main__":
    tst = [123, 122, 111, 222, 1000, 0, 2000]
    for ts in tst:
        print(f"Количество четных и нечетных цифр в числе {ts} равно: {digits(ts)}")
