"""
Задание 1.

Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего

Подсказка:
Для решения задачи обязательно примените коллекцию из модуля collections
Для лучшего освоения материала можете сделать
несколько варианто решения этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога
Предприятия, с прибылью ниже среднего значения: Копыта
"""
from collections import defaultdict, namedtuple


def comp_defdict():
    n = None
    companies = defaultdict(list)
    avg_sum = 0.0
    while not n:
        try:
            n = int(input("Введите количество предприятий для расчета прибыли: "))
        except ValueError:
            print("Ожидалось число!")
    for i in range(n):
        name = input("Введите название предприятия: ")
        a = b = c = d = None
        while not (a and b and c and d):
            print("через пробел введите прибыль данного предприятия")
            print("за каждый квартал(Всего 4 квартала): ", end="")
            try:
                a, b, c, d = map(int, input().split())
            except ValueError:
                print("Ожидалось 4 числа через пробел!")
        companies[name] = [a, b, c, d]
        avg_sum += a + b + c + d
    avg_sum /= n
    print("Средняя годовая прибыль всех предприятий:", avg_sum)
    top = ""
    low = ""
    for cmp in companies:
        cmp_sum = sum(companies[cmp])
        if cmp_sum >= avg_sum:
            top = f'{top}, {cmp}'
        else:
            low = f'{low}, {cmp}'
    top = top[2:]
    low = low[2:]
    print("Предприятия с прибылью выше средней:", top)
    if len(low) > 0:
        print("Компании с прибылью ниже средней:", low)


def comp_nmtupl():
    n = None
    company = namedtuple('company', 'name q1 q2 q3 q4 summ')
    companies = []
    avg_sum = 0.0
    while not n:
        try:
            n = int(input("Введите количество предприятий для расчета прибыли: "))
        except ValueError:
            print("Ожидалось число!")
    for i in range(n):
        name = input("Введите название предприятия: ")
        a = b = c = d = None
        while not (a and b and c and d):
            print("через пробел введите прибыль данного предприятия")
            print("за каждый квартал(Всего 4 квартала): ", end="")
            try:
                a, b, c, d = map(int, input().split())
            except ValueError:
                print("Ожидалось 4 числа через пробел!")
        summ = sum([a, b, c, d])
        comp = company(name, a, b, c, d, summ)
        companies.append(comp)
        avg_sum += summ
    avg_sum /= n
    print("Средняя годовая прибыль всех предприятий:", avg_sum)
    top = ""
    low = ""
    for cmp in companies:
        if cmp.summ >= avg_sum:
            top = f'{top}, {cmp.name}'
        else:
            low = f'{low}, {cmp.name}'
    top = top[2:]
    low = low[2:]
    print("Предприятия с прибылью выше средней:", top)
    if len(low) > 0:
        print("Компании с прибылью ниже средней:", low)


if __name__ == "__main__":
    #comp_defdict()
    comp_nmtupl()
