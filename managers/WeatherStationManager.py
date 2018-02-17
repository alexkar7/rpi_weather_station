"""
Main project class. This class controls all the behaviour for my weather station
"""
# *** IMPORTS *** #
from sensors.logicals.HumiditySensor import HumiditySensor
from sensors.logicals.TemperatureSensor import TemperatureSensor


# *** CLASS *** #
class WeatherStationManager(object):

    # *** INIT *** #
    def __init__(self):

        self.humidity_sensor = HumiditySensor()
        self.temperature_sensor = TemperatureSensor()

    # *** API *** #
    def get_temperature(self):
        return self.humidity_sensor.get_humidity()

    def get_humidity(self):
        return self.temperature_sensor.get_temperature()
