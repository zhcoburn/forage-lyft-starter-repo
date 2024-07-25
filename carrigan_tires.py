from tire import Tire
from abc import ABC


class CarriganTires(Tire):
    def __init__(self, tire_values: list):
        self.tire_values = tire_values

    def needs_service(self):
        for x in self.tire_values:
            if x >= 0.9:
                return True
        return False
