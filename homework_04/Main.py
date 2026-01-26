import datetime
from PhotoClass import Photo
from AudioClass import Audio
from VideoClass import Video
from Storage import *

print("=== СОЗДАЕМ ФАЙЛЫ ===")

# Создаем фото
my_photo = Photo(
    filename="отпуск.jpg",
    size=2048000,  # 2 МБ
    owner="Маша",
    file_date=datetime.datetime.now(),
    resolution="4032x3024",
    camera="Canon EOS"
)

# Создаем музыку
my_music = Audio(
    filename="любимая_песня.mp3",
    size=5120000,  # 5 МБ
    owner="Петя",
    file_date=datetime.datetime.now(),
    duration=240,
    artist="Группа 'Луна'"
)

# Создаем видео
my_video = Video(
    filename="котик.mp4",
    size=15728640,  # 15 МБ
    owner="Вася",
    file_date=datetime.datetime.now(),
    duration=60,
    quality="HD"
)

print("\n=== СМОТРИМ ИНФОРМАЦИЮ ===")
print(my_photo.get_info())
print(my_music.get_info())
print(my_video.get_info())

print("\n=== ИСПОЛЬЗУЕМ ОБЩИЕ МЕТОДЫ ===")
# Все объекты имеют методы rename() и show_type()
my_photo.rename("лучшая_фотка.jpg")
my_music.rename("супер_хит.mp3")

# Полиморфизм: один метод, разные реализации
files = [my_photo, my_music, my_video]
for file in files:
    file.show_type()  # Каждый файл покажет свой тип!

print("\n=== ИСПОЛЬЗУЕМ СПЕЦИАЛЬНЫЕ МЕТОДЫ ===")
my_photo.open()  # Только для фото
my_music.play()  # Только для аудио
my_video.extract_frame(10, 50)  # Только для видео

# Создаем разные хранилища
computer = LocalStorage()
yandex_disk = CloudStorage("Яндекс.Диск")
phone = PhoneStorage()

# Сохраняем в разные места
print("\n--- Сохраняем файл в разные места ---")
computer.save(my_photo)
yandex_disk.save(my_photo)
phone.save(my_photo)

# Используем специальные методы каждого хранилища
print("\n--- Особые возможности хранилищ ---")
print(f"На компьютере: {computer.get_free_space()}")
print(f"Ссылка из облака: {yandex_disk.share_link(my_photo)}")
print(f"Нужно ли оптимизировать для телефона: {phone.needs_optimization(my_photo)}")

""" ВОПРОС: Много ли кода придется дописать/переписать 
    при добавлении новых типов файлов и способов их хранения?
    
    ОТВЕТ: Мало
    
    Для добавления нового типа файла (например, PDF):
    1. Создать новый класс (например, Document)
    2. Унаследовать его от MediaFile
    3. Добавить свои свойства и методы
    
    НЕ НУЖНО:
    - Менять старый код
    - Переписывать другие классы"""