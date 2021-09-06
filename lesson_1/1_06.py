"""6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква."""

number_symbol = int(input("Введите номер символа ('a'=1, 'z'=26): "))

number_symbol_ord = number_symbol + ord('a') - 1

if ord('a') <= number_symbol_ord <= ord('z'):
    print(f"Вы указали код символа {chr(number_symbol_ord)}")
else:
    print("Неверный ввод")
