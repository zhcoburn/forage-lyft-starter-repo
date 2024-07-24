from abc import ABC
from datetime import date
from spindler_battery import SpindlerBattery
from nubbin_battery import NubbinBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from car import Car


class CarFactory(ABC):

    def create_calliope(self, current_date: date, last_service: date, current_mileage: int, last_service_mileage: int):
        engine = CapuletEngine(current_mileage,last_service_mileage)
        battery = SpindlerBattery(current_date, last_service)
        new_car = Car(last_service, engine, battery)
        return new_car

    def create_glissade(self, current_date: date, last_service: date, current_mileage: int, last_service_mileage: int):
        engine = WilloughbyEngine(current_mileage,last_service_mileage)
        battery = SpindlerBattery(current_date, last_service)
        new_car = Car(last_service, engine, battery)
        return new_car

    def create_palindrome(self, current_date: date, last_service: date, warning_light_is_on: bool):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(current_date, last_service)
        new_car = Car(last_service, engine, battery)
        return new_car

    def create_rorschach(self, current_date: date, last_service: date, current_mileage: int, last_service_mileage: int):
        engine = WilloughbyEngine(current_mileage,last_service_mileage)
        battery = NubbinBattery(current_date, last_service)
        new_car = Car(last_service, engine, battery)
        return new_car

    def create_thovex(self, current_date: date, last_service: date, current_mileage: int, last_service_mileage: int):
        engine = CapuletEngine(current_mileage,last_service_mileage)
        battery = NubbinBattery(current_date, last_service)
        new_car = Car(last_service, engine, battery)
        return new_car