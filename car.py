from abc import ABC, abstractmethod
from serviceable import Serviceable
from datetime import date
from engine.engine import Engine
from battery import Battery
from tire import Tire


class Car(Serviceable):
    def __init__(self, last_service_date: date, engine: Engine, battery: Battery, tires: Tire):
        self.last_service_date = last_service_date
        self.engine = engine
        self.battery = battery
        self.tires = tires

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service() or self.tires.needs_service()
