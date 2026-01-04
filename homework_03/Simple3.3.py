"""Написать функцию, которая создаёт абсолютный путь к файлу.
Позиционные аргументы:
название диска,
неограниченное количество папок,
имя файла (без расширения).
Ключевые аргументы:
ext — расширение файла,
sep — разделитель (по умолчанию '/').

Пример:
full_path('c:', 'work', 'python', 'function', 'main', ext='py') ➜ 'c:/work/python/function/main.py'"""

def full_path(*args, ext, sep = "/"):
    return sep.join(args) + "." + ext

print(full_path('c:', 'work', 'python', 'function', 'main', ext='py') )

