"""
Задание 2.

Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Попытайтесь решить это задание в двух вариантах
1) через collections

defaultdict(list)
int(, 16)
reduce

2) через ООП

вспомните про перегрузку методов

__mul__
__add__
"""
from collections import defaultdict


class MyHexNum:

    def __init__(self, value):
        self.value = value

    def __mul__(self, other):
        return hex(int(self.value, 16) * int(other.value, 16))[2:]

    def __add__(self, other):
        return hex(int(self.value, 16) + int(other.value, 16))[2:]

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value


if __name__ == "__main__":
    def_dict = defaultdict(list)
    a = input('Введите первое 16-ричное число : 0x')
    b = input('Введите второе 16-ричное число : 0x')
    def_dict[a] = list(a)
    def_dict[b] = list(b)
    summ = hex(int(''.join(def_dict[a]), 16) + int(''.join(def_dict[b]), 16))[2:]
    def_dict[summ] = list(summ)
    mul = hex(int(''.join(def_dict[a]), 16) * int(''.join(def_dict[b]), 16))[2:]
    def_dict[mul] = list(mul)
    print('Сумма чисел :', def_dict[summ])
    print('Произведение чисел :', def_dict[mul])

    print('Через ООП:')
    a = MyHexNum(input('Введите первое 16-ричное число : 0x'))
    b = MyHexNum(input('Введите второе 16-ричное число : 0x'))
    print('Сумма чисел :', a + b)
    print('Произведение чисел :', a * b)
