"""Написать программу, которая удаляет из списка все дубликаты, сохранив исходный порядок элементов."""

my_list = [1, 2, 1, "a", 3, 2, "b", "a", "c", 1, 4, 3, 1, 2, 5, 5]
print(my_list)

for ind in range(len(my_list) - 1):
    if ind > len(my_list) - 2:
        break
    while my_list.count(my_list[ind]) > 1:
        my_list.pop(my_list.index(my_list[ind], ind + 1))

print(my_list)

