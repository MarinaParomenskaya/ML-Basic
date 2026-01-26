# Базовый класс для всех медиа - файлов
# общая информация, которая есть у всех файлов

class MediaFile:
    def __init__(self, filename, size, owner, file_date):
        self.filename = filename
        self.size = size
        self.owner = owner
        self.created_at = file_date

    def get_info(self):
        info = f" Имя файла: {self.filename} Размер: {self.size} байт Владелец: {self.owner} Создан: {self.created_at}"
        return info

    def rename(self, new_name):
        self.filename = new_name
        print(f"Файл переименован в '{new_name}'")

    def show_type(self):
        print(self.filename, " - это медиа-файл")