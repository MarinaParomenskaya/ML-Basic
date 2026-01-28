"""
В модуле car создайте класс Car
класс Car должен быть наследником Vehicle
добавьте атрибут engine классу Car
объявите метод set_engine, который принимает в себя экземпляр объекта Engine и
    устанавливает на текущий экземпляр Car
"""

from homework_05.base import Vehicle
from homework_05.engine import Engine


class Car(Vehicle):
   engine: Engine

   def set_engine(self, engine):
       self.engine = engine

