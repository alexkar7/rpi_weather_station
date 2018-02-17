"""
A class to get current temperature. By default we use DHT11 sensor
"""

# *** IMPORTS *** #
import os
from ..physicals.DHT11 import DHT11

# *** CONSTANTS ***
DHT11_GPIO_PIN = "DHT11_GPIO_PIN"


# *** CLASS *** #
class TemperatureSensor(object):

    # *** INIT *** #
    def __init__(self):
        self.physical_sensor = DHT11(self.get_dht11_gpio_pin())

    # *** API *** #
    def get_temperature(self):
        return self.physical_sensor.get_temperature()

    # *** PRIVATE *** #
    def get_dht11_gpio_pin(self):

        try:

            gpio_pin = int(os.environ[DHT11_GPIO_PIN])

            return gpio_pin

        except KeyError as exc:
            print("Can't get DHT11 GPIO port environment variable to config the sensor. Details = %s" % str(exc))
            raise
