from BaseClass import MediaFile

# Класс для аудиофайлов
class Audio(MediaFile):

    def __init__(self, filename, size, owner, file_date, duration, artist=""):
        super().__init__(filename, size, owner, file_date)
        self.duration = duration  # Длительность в секундах
        self.artist = artist  # Исполнитель

    def get_info(self):
        base_info = super().get_info()
        audio_info = f"Тип: Аудиофайл, Длительность: {self.duration} сек, Исполнитель: {self.artist if self.artist else 'неизвестен'}"
        return base_info + audio_info

    def show_type(self):
        print(self.filename, "- это музыкальный файл!")

    def play(self):
        """Метод, который есть ТОЛЬКО у аудио"""
        print(f"Играю трек: {self.filename}")
