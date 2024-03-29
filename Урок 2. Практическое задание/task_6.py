"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""
from random import randint


def my_int(a: str) -> int:
    res = int(a)
    if res < 0 or res > 100:
        raise ValueError
    return res


def guess_number(numb: int, n=10):
    if n == 10:
        print("Я загадал число от 0 до 100, попробуйте отгадать: ", end="")
    if n < 1:
        print()
        print(f'Я загадывал число {numb}, к сожалению вы не смогли отгадать за 10 попыток')
        return
    a = input()
    try:
        a = my_int(a)
    except ValueError:
        print("Можно вводить только числа от 0 до 100, попробуйте еще раз: ", end="")
        guess_number(numb, n=n - 1)
        return
    if a == numb:
        print("Вы отгадали!")
        return
    elif a > numb and n != 1:
        print(f"Я загадал число меньше {a}, попробуйте еще раз: ", end="")
    elif a < numb and n != 1:
        print(f"Я загадал число больше {a}, попробуйте еще раз: ", end="")
    guess_number(numb, n=n-1)


if __name__ == "__main__":
    guess_number(randint(0, 100))

