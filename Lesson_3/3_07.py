"""7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться."""

import random

r = [random.randint(0, 99) for _ in range(100)]
print(f'Массив: {r}')

sort_list = []
sort_list.extend(r)
sort_list.sort()
print(f'Два наименьших элемента: {sort_list[0]} и {sort_list[1]}')
