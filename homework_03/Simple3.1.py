"""Написать функцию, которая принимает неограниченное количество
чисел в виде позиционных аргументов и ключевой аргумент
— операцию над этими числами (сложение или умножение).
Функция должна возвращать результат выполнения указанной операции."""

def calculator(*args, operation: str):
    if operation == '+':
        return sum(args)
    elif operation == '*':
        mul = lambda lst:lst[0] * mul(lst[1:]) if lst else 1
        return mul(args)
    else:
        return 0

print(calculator(1,2,3,4,5,operation ="+"))
print(calculator(2,3,5, operation = "*"))
