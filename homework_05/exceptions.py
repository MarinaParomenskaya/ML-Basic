"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""

class LowFuelError(Exception):
    def __init__(self):
        print('Ошибка: в машине нет бензина.')

class NotEnoughFuel(Exception):
    def __init__(self, fuel, distance, fuel_need):
        print(f'Ошибка: для того, чтобы проехать {distance} км. необходимо {fuel_need} л. топлива.'
            f'В наличии только {fuel} л.')

class CargoOverload(Exception):
    def __init__(self, max_cargo):
        print(f'Ошибка: превышен максимальный вес {max_cargo}кг.')
