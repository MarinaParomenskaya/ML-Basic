"""Написать функцию для ввода из консоли целого числа.
Если введено не число, функция должна вывести соответствующее
сообщение и предложить ввести значение заново — до тех пор,
пока пользователь не введёт корректное число"""

def is_digit(lc_str: str) -> bool:
    if lc_str.isdigit():
        print(lc_str, " is a number!")
        return True
    else:
        print("Try again")
        return False

input_str = input("Enter a number: ")
while not is_digit(input_str):
    input_str = input("Enter a number: ")

