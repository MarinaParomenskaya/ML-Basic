class Storage:
    """Базовый класс для хранения файлов"""

    def save(self, file):
        """Сохранить файл"""
        print(f"Сохраняю {file.filename} в хранилище")

    def load(self, filename):
        """Загрузить файл"""
        print(f"Загружаю {filename} из хранилища")
        # Здесь был бы код загрузки

class LocalStorage(Storage):
    """Хранилище на компьютере"""

    def save(self, file):
        print(f"Сохраняю {file.filename} на жесткий диск в папку 'Документы'")

    def get_free_space(self):
        """Только у локального хранилища"""
        return "500 ГБ свободно"


class CloudStorage(Storage):
    """Хранилище в интернете (облако)"""

    def __init__(self, service_name):
        self.service_name = service_name  # Например, "Яндекс.Диск"

    def save(self, file):
        print(f"Загружаю {file.filename} в {self.service_name}")

    def share_link(self, file):
        """Только у облачного хранилища - получить ссылку"""
        return f"https://cloud.ru/share/{file.filename}"


class PhoneStorage(Storage):
    """Хранилище на телефоне"""

    def save(self, file):
        print(f"Сохраняю {file.filename} в память телефона")

    def needs_optimization(self, file):
        """Только для телефона - нужно ли оптимизировать размер"""
        return file.size > 10000000  # Больше 10 МБ