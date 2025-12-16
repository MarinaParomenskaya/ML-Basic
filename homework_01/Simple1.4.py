"""Пользователь вводит строку, содержащую любые символы
(буквы, цифры и специальные символы).
Программа должна вычислить и вывести сумму всех цифр, присутствующих в этой строке."""

input_str = input("Your string: ")

sum = 0
for letter in input_str:
    if letter.isdigit():
        sum += int(letter)

print("The result is: ", sum)