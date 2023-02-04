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

Это файл для пятого скрипта



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
from recordclass import recordclass


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


@profile
def fill_workers():
    workers = []
    for i in range(10000):
        workers.append(Worker(f'иван {i}', f'иванов {i}', 'сварщик',
                              {'wage': randint(25000, 100000), 'bonus': randint(25000, 100000)}))
    return workers


@profile
def fill_workers_rc():
    WorkerRC = recordclass('WorkerRC', 'name surname position income')
    workers_rc_list = []
    for i in range(10000):
        workers_rc_list.append(WorkerRC(f'иван {i}', f'иванов {i}', 'сварщик',
                                        {'wage': randint(25000, 100000), 'bonus': randint(25000, 100000)}))
    return workers_rc_list


if __name__ == '__main__':
    a = fill_workers()
    del a
    a = fill_workers_rc()
    #print(a[0].name, a[0].surname, a[0].position, a[0].income)
    del a

"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    98     19.7 MiB     19.7 MiB           1   @profile
    99                                         def fill_workers():
   100     19.7 MiB      0.0 MiB           1       workers = []
   101     27.1 MiB      0.0 MiB       10001       for i in range(10000):
   102     27.1 MiB      4.4 MiB       20000           workers.append(Worker(f'иван {i}', f'иванов {i}', 'сварщик',
   103     27.1 MiB      3.0 MiB       10000                                 {'wage': randint(25000, 100000), 'bonus': 
   104     27.1 MiB      0.0 MiB           1       return workers



Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
   107     20.6 MiB     20.6 MiB           1   @profile
   108                                         def fill_workers_rc():
   109     20.6 MiB      0.0 MiB           1       WorkerRC = recordclass('WorkerRC', 'name surname position income')
   110     20.6 MiB      0.0 MiB           1       workers_rc_list = []
   111     25.1 MiB      0.0 MiB       10001       for i in range(10000):
   112     25.1 MiB      2.7 MiB       20000           workers_rc_list.append(WorkerRC(f'иван {i}', f'иванов {i}', 'сва
   113     25.1 MiB      1.8 MiB       10000                                           {'wage': randint(25000, 100000),
   114     25.1 MiB      0.0 MiB           1       return workers_rc_list



recordclass вместо ооп тоже позволяет экономить память

"""
