"""
В модуле plane создайте класс Plane
класс Plane должен быть наследником Vehicle
добавьте атрибуты cargo и max_cargo классу Plane
добавьте max_cargo в инициализатор (переопределите родительский)
объявите метод load_cargo, который принимает число, проверяет, что в сумме
    с текущим cargo не будет перегруза, и обновляет значение, в ином случае выкидывает
    исключение exceptions.CargoOverload
объявите метод remove_all_cargo, который обнуляет значение cargo и возвращает значение cargo,
    которое было до обнуления
"""
from homework_05.base import Vehicle
from homework_05.exceptions import CargoOverload


class Plane(Vehicle):
    cargo: int
    max_cargo: int

    def __init__(self, max_cargo: int):
        super().__init__()
        self.max_cargo = max_cargo

    def load_cargo(self, add_cargo):
        if self.cargo + add_cargo <= self.max_cargo:
            self.cargo += add_cargo
        else:
            raise CargoOverload(self.max_cargo)

    def remove_all_cargo(self):
        save_cargo = self.cargo
        self.cargo = 0

        return save_cargo
