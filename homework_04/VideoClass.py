from BaseClass import MediaFile

"""Класс для видеофайлов. Унаследован от MediaFile"""
class Video(MediaFile):

    def __init__(self, filename, size, owner, file_date, duration, quality):
        super().__init__(filename, size, owner, file_date)
        self.duration = duration
        self.quality = quality  # Например, "HD", "FullHD"

    def get_info(self):
        base_info = super().get_info()
        video_info = f"Тип: Видеофайл, Длительность: {self.duration} сек, Качество: {self.quality}"
        return base_info + video_info

    def show_type(self):
        print(self.filename, "- это видео!")

    def extract_frame(self, second_from, secont_to):
        """Извлечь ролик"""
        print(f"Извлекаю ролик с {second_from} по {secont_to}")