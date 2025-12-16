"""Классическая игра FizzBuzz. Программа в цикле выводит в консоль числа от 1 до 100.
Если число кратно 3, вместо него выводится Fizz.
Если кратно 5 — Buzz.
Если кратно и 3, и 5 — FizzBuzz."""

for i in range(1, 101):
    str_result = ''
    if i % 3 == 0:
        str_result += 'Fizz'
    if i % 5 == 0:
        str_result += 'Buzz'

    if len(str_result) == 0:
        print(i)
        continue

    print(str_result)