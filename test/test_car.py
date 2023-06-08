import unittest
from datetime import datetime

from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex


class CarServiceTest(unittest.TestCase):
    def setUp(self):
        self.today = datetime.today().date()

    def test_battery_should_be_serviced(self):
        car_models = [Calliope, Glissade, Palindrome, Rorschach, Thovex]
        last_service_dates = [self.today.replace(year=self.today.year - 3),  # Calliope
                              self.today.replace(year=self.today.year - 3),  # Glissade
                              self.today.replace(year=self.today.year - 5),  # Palindrome
                              self.today.replace(year=self.today.year - 5),  # Rorschach
                              self.today.replace(year=self.today.year - 5)]  # Thovex

        for car_model, last_service_date in zip(car_models, last_service_dates):
            car = car_model(last_service_date, 0, 0)
            self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        car_models = [Calliope, Glissade, Palindrome, Rorschach, Thovex]
        last_service_dates = [self.today.replace(year=self.today.year - 1),  # Calliope
                              self.today.replace(year=self.today.year - 1),  # Glissade
                              self.today.replace(year=self.today.year - 3),  # Palindrome
                              self.today.replace(year=self.today.year - 3),  # Rorschach
                              self.today.replace(year=self.today.year - 3)]  # Thovex

        for car_model, last_service_date in zip(car_models, last_service_dates):
            car = car_model(last_service_date, 0, 0)
            self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        car_models = [Calliope, Glissade, Palindrome, Rorschach, Thovex]
        last_service_dates = [self.today,  # Calliope
                              self.today,  # Glissade
                              self.today,  # Palindrome
                              self.today,  # Rorschach
                              self.today]  # Thovex
        current_mileages = [30001,  # Calliope
                            60001,  # Glissade
                            0,       # Palindrome
                            60001,  # Rorschach
                            30001]  # Thovex

        for car_model, last_service_date, current_mileage in zip(car_models, last_service_dates, current_mileages):
            car = car_model(last_service_date, current_mileage, 0)
            self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        car_models = [Calliope, Glissade, Palindrome, Rorschach, Thovex]
        last_service_dates = [self.today,  # Calliope
                              self.today,  # Glissade
                              self.today,  # Palindrome
                              self.today,  # Rorschach
                              self.today]  # Thovex
        current_mileages = [30000,  # Calliope
                            60000,  # Glissade
                            0,       # Palindrome
                            60000,  # Rorschach
                            30000]  # Thovex

        for car_model, last_service_date, current_mileage in zip(car_models, last_service_dates, current_mileages):
            car = car_model(last_service_date, current_mileage, 0)
            self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
