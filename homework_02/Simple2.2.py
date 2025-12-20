"""Дана строка текста (или введённая через консоль).
Программа должна вернуть новую строку, в которой порядок слов будет обратным.
Пример:
"Python is really cool" → "cool really is Python"."""

input_str = "Python is really cool"

reverse_string = input_str.split(" ")[::-1]

print("The result is: ", " ".join(reverse_string))