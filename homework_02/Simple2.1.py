"""Написать программу, которая получает на вход строку и возвращает словарь, где:
ключи — символы из этой строки;
значения — количество раз, сколько каждый символ встречается."""

input_str = input("Your string: ")
dct = {letter: input_str.count(letter) for letter in input_str}

print("The result is: ", dct)
