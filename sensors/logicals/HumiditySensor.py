"""
HumiditySensor class gets current humidity information using DHT11 and DHT22 sensors
"""

# *** IMPORTS *** #
import os
from ..physicals.DHT11 import DHT11
from ..physicals.DHT22 import DHT22

# *** CONSTANTS ***
DHT11_GPIO_PIN = "DHT11_GPIO_PIN"
DHT22_GPIO_PIN = "DHT22_GPIO_PIN"


# *** CLASS *** #
class HumiditySensor(object):

    # *** INIT *** #
    def __init__(self):
        self.dht11_sensor = DHT11(self.get_DHT11_gpio_pin())
        self.dht22_sensor = DHT22(self.get_DHT22_gpio_pin())

    # *** API *** #
    def get_humidity(self):

        humidity = {
            'dht11': self.dht11_sensor.get_humidity(),
            'dht22': self.dht22_sensor.get_humidity()
        }

        return humidity

    # *** PRIVATE *** #
    def get_DHT11_gpio_pin(self):

        try:

            gpio_pin = int(os.environ[DHT11_GPIO_PIN])

            return gpio_pin

        except KeyError as exc:
            print("Can't get DHT11 GPIO port environment variable to config the sensor. Details = %s" % str(exc))
            raise

    def get_DHT22_gpio_pin(self):

        try:

            gpio_pin = int(os.environ[DHT22_GPIO_PIN])

            return gpio_pin

        except KeyError as exc:
            print("Can't get DHT22 GPIO port environment variable to config the sensor. Details = %s" % str(exc))
            raise
