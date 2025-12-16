"""Пользователь вводит строку через консоль (состоящую только из букв в разном регистре).
Программа должна создать новую строку, содержащую только те буквы из исходной строки,
которые были в верхнем регистре."""
#Для любой строки: sdvsdfvMomosa9d-0pl -0o-0ak- A 0dslv[lp Mpl=sal Apls,dv9302j = MAMA

input_str = input("Your string: ")

upper_str = input_str.upper()
result_str = ""

for i in range(len(input_str)):
    if input_str[i] == upper_str[i] and upper_str[i] != upper_str[i].lower():
        result_str += input_str[i]

print("The result is: ", result_str)