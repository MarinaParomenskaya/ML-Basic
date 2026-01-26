from BaseClass import MediaFile

"""Класс для фотографий. Унаследован от MediaFile"""
class Photo(MediaFile):
    def __init__(self, filename, size, owner, file_date, resolution, camera=""):
        super().__init__(filename, size, owner, file_date)  # Вызываем конструктор родителя
        # Добавляем свойства, характерные для фото
        self.resolution = resolution  # Например, "1920x1080"
        self.camera = camera  # Например, "iPhone 12"

    def get_info(self):
        """Переопределяем метод: добавляем информацию о фото"""
        base_info = super().get_info()  # Берем базовую информацию
        photo_info = f"Тип: Фотография, Разрешение: {self.resolution} Камера: {self.camera if self.camera else 'не указано'}"
        return base_info + photo_info

    def show_type(self):
        print(self.filename, "- это фотография.")

    def open(self):
        """Метод, который есть ТОЛЬКО у фото"""
        print(f"Открываю в paint: {self.filename}")