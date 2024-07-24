from abc import ABC, abstractmethod
from serviceable import Serviceable
from datetime import date
from engine.engine import Engine
from battery import Battery


class Car(Serviceable):
    def __init__(self, last_service_date: date, engine: Engine, battery: Battery):
        self.last_service_date = last_service_date
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()
