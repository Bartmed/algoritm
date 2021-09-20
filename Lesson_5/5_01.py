"""1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести
наименования предприятий, чья прибыль ниже среднего.
Примечание: для решения задач попробуйте применить какую-нибудь коллекцию из
модуля collections"""

from collections import namedtuple
from statistics import mean

New_Company = namedtuple('New_Company', 'name profit_list avg')

lst = []
for i in range(int(input('Введите количество компани '))):
    arg = input('Введите в строку имя и поквартальную прибыль через пробел:\n').split()
    lst.append(New_Company(arg[0], arg[1:], mean(map(int, arg[1:3]))))

avg = mean([i.avg for i in lst])

for i in lst:
    print(f'Компания: {i.name} \t\tСредняя прибыль за год: {i.avg}')

print('_' * 70, '\n')

print('Компании с прибылью меньше средней:')
for i in lst:
    if i.avg < avg:
        print(i.name)

print('Компании с прибылью больше средней:')
for i in lst:
    if i.avg > avg:
        print(i.name)
