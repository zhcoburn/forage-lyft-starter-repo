from abc import ABC, abstractmethod
from datetime import date


class Battery(ABC):
    @abstractmethod
    def needs_service(self):
        pass