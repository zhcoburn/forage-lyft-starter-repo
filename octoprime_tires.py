from tire import Tire
from abc import ABC


class OctoprimeTires(Tire):
    def __init__(self, tire_values: list):
        self.tire_values = tire_values

    def needs_service(self):
        tire_sum = 0.0
        for x in self.tire_values:
            tire_sum = tire_sum + x
        if tire_sum >= 3.0:
            return True
        else:
            return False
