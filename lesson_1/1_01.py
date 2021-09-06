"""1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь."""

number = input('Введите число: ')

sum = 0
prod = 1

for i in number:
    sum += int(i)
    prod *= int(i)
print(f"Сумма цифр числа {number}: {sum}")
print(f"Произведение цифр: {number}: {prod}")
