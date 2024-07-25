import unittest
from datetime import datetime
from datetime import date
from carrigan_tires import CarriganTires
from octoprime_tires import OctoprimeTires


class TestCarrigan(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        tire_vals = [0.8, 0.9, 0.3, 0.95]

        tires = CarriganTires(tire_vals)
        self.assertTrue(tires.needs_service())

    def test_tires_should_not_be_serviced(self):
        tire_vals = [0.5, 0.85, 0.8, 0.29]

        tires = CarriganTires(tire_vals)
        self.assertFalse(tires.needs_service())


class TestOctoprime(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        tire_vals = [0.8, 0.6, 0.75, 0.85]

        tires = OctoprimeTires(tire_vals)
        self.assertTrue(tires.needs_service())

    def test_tires_should_not_be_serviced(self):
        tire_vals = [0.5, 0.65, 0.8, 0.29]

        tires = OctoprimeTires(tire_vals)
        self.assertFalse(tires.needs_service())


if __name__ == '__main__':
    unittest.main()
