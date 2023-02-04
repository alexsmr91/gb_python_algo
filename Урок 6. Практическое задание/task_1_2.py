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

Это файл для второго скрипта

ДЗ 9 из курса основ, задача 3

Реализовать базовый класс Worker (работник):
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы «оклад» и «премия», например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.

"""
from random import randint
from memory_profiler import profile


class Worker:
    name = ''
    surname = ''
    position = ''
    _income = {"wage": 0, "bonus": 0}

    def __init__(self, name: str, surname: str, position: str, income: dict):
        # Ваш код здесь
        self.name = name.capitalize()
        self.surname = surname.capitalize()
        self.position = position.capitalize()
        self._income = income

    def get_full_name(self) -> str:
        """Возвращает строку по формату 'Имя Фамилия'"""
        # Ваш код здесь
        return f'{self.name} {self.surname}'

    def get_total_income(self) -> int:
        """Возвращает суммарный ежемесячных доход"""
        # Ваш код здесь
        return self._income['wage'] + self._income['bonus']

    class Worker:
        name = ''
        surname = ''
        position = ''
        _income = {"wage": 0, "bonus": 0}

        def __init__(self, name: str, surname: str, position: str, income: dict):
            # Ваш код здесь
            self.name = name.capitalize()
            self.surname = surname.capitalize()
            self.position = position.capitalize()
            self._income = income

        def get_full_name(self) -> str:
            """Возвращает строку по формату 'Имя Фамилия'"""
            # Ваш код здесь
            return f'{self.name} {self.surname}'

        def get_total_income(self) -> int:
            """Возвращает суммарный ежемесячных доход"""
            # Ваш код здесь
            return self._income['wage'] + self._income['bonus']


class WorkerSlots:
    __slots__ = ('name', 'surname', 'position', '_income',)

    def __init__(self, name: str, surname: str, position: str, income: dict):
        # Ваш код здесь
        self.name = name.capitalize()
        self.surname = surname.capitalize()
        self.position = position.capitalize()
        self._income = income

    def get_full_name(self) -> str:
        """Возвращает строку по формату 'Имя Фамилия'"""
        # Ваш код здесь
        return f'{self.name} {self.surname}'

    def get_total_income(self) -> int:
        """Возвращает суммарный ежемесячных доход"""
        # Ваш код здесь
        return self._income['wage'] + self._income['bonus']


@profile
def fill_workers():
    workers = []
    for i in range(10000):
        workers.append(Worker(f'иван {i}', f'иванов {i}', 'сварщик',
                              {'wage': randint(25000, 100000), 'bonus': randint(25000, 100000)}))
    return workers


@profile
def fill_workers_slots():
    workers_slots = []
    for i in range(10000):
        workers_slots.append(WorkerSlots(f'иван {i}', f'иванов {i}', 'сварщик',
                                         {'wage': randint(25000, 100000), 'bonus': randint(25000, 100000)}))
    return workers_slots


if __name__ == '__main__':
    a = fill_workers()
    del a
    a = fill_workers_slots()
    del a

"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
   110     19.4 MiB     19.4 MiB           1   @profile
   111                                         def fill_workers():
   112     19.4 MiB      0.0 MiB           1       workers = []
   113     26.9 MiB      0.2 MiB       10001       for i in range(10000):
   114     26.9 MiB      5.4 MiB       20000           workers.append(Worker(f'иван {i}', f'иванов {i}', 'сварщик',
   115     26.9 MiB      1.9 MiB       10000                                 {'wage': randint(25000, 100000), 'bonus': randint(25000, 100000)}))
   116     26.9 MiB      0.0 MiB           1       return workers


Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
   119     20.1 MiB     20.1 MiB           1   @profile
   120                                         def fill_workers_slots():
   121     20.1 MiB      0.0 MiB           1       workers_slots = []
   122     26.0 MiB      0.1 MiB       10001       for i in range(10000):
   123     26.0 MiB      4.1 MiB       20000           workers_slots.append(WorkerSlots(f'иван {i}', f'иванов {i}', 'сварщик',
   124     26.0 MiB      1.6 MiB       10000                                            {'wage': randint(25000, 100000), 'bonus': randint(25000, 100000)}))
   125     26.0 MiB      0.0 MiB           1       return workers_slots


Класс со слотами потребляет меньше памяти
"""