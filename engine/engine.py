from abc import ABC, abstractmethod
from datetime import datetime

class Engine(ABC):
    @abstractmethod
    def needs_service(self):
        pass