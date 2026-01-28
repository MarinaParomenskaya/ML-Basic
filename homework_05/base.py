"""
Доработайте базовый класс base.Vehicle:
добавьте атрибуты weight, started, fuel, fuel_consumption со значениями по умолчанию
добавьте инициализатор для установки weight, fuel, fuel_consumption
добавьте метод start. При вызове этого метода необходимо проверить состояние started.
    И если не started, то нужно проверить, что топлива больше нуля, и обновить состояние started,
    иначе нужно выкинуть исключение exceptions.LowFuelError
добавьте метод move, который проверяет, что топлива достаточно для преодоления переданной дистанции
    (вплоть до полного расхода), и изменяет количество оставшегося топлива, иначе выкидывает исключение
    exceptions.NotEnoughFuel
"""

from abc import ABC
from homework_05.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):

    def __init__(self, weight = 3.5, fuel = 20, fuel_consumption = 5):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption # литров на 100 км.
        self.started = False

    def start(self):
        if self.started:
            print('Машина уже заведена.')
        else:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError

    def move(self, distance):
        fuel_need = self.fuel_consumption * distance / 100
        if self.fuel >= fuel_need:
            self.fuel -= fuel_need
        else:
            raise NotEnoughFuel(self.fuel, distance, fuel_need)

