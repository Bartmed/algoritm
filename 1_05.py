"""5. Пользователь вводит две буквы.
Определить, на каких местах алфавита они стоят и сколько между ними находится букв."""

first = input("Введите первый символ от 'a' до 'z': ")
second = input("Введите второй символ от 'a' до 'z': ")

code_first = ord(first)
code_second = ord(second)

if code_first < code_second:
    poz_1 = code_first - ord('a') + 1
    poz_2 = code_second - ord('a') + 1
    print(f"Позиция '{first}' = {poz_1}, позиция '{second}' = {poz_2}, букв между ними: {poz_2 - poz_1 - 1}")
else:
    print("Неверный ввод")
