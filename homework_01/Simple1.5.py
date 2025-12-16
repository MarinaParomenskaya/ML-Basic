"""Пользователь вводит через консоль 10 чисел. П
рограмма должна определить максимальное число и вывести его в консоль."""

max_number = None
for i in range(10):
    input_number = input("Your number: ")

    if input_number.isdigit() and max_number is None:
        max_number = int(input_number)
        continue

    if input_number.isdigit() and int(input_number) > max_number:
        max_number = int(input_number)

print("The max number is: ", max_number)
