"""
DHT11 class gets current temperature and humidity values from DHT11 sensor device
"""

# *** IMPORTS *** #
import Adafruit_DHT


# *** CLASS *** #
class DHT11(object):

    sensor = Adafruit_DHT.DHT11

    # *** INIT *** #
    def __init__(self,
                 gpio_pin):

        self.gpio_pin = gpio_pin

    # *** API *** #
    """
    Get current humidity
    """
    def get_humidity(self):

        humidity = None

        while humidity is None:
            humidity, temperature = Adafruit_DHT.read_retry(DHT11.sensor, self.gpio_pin)

        return humidity

    """
    Get current temperature
    """
    def get_temperature(self):

        temperature = None

        while temperature is None:
            humidity, temperature = Adafruit_DHT.read_retry(DHT11.sensor, self.gpio_pin)

        return temperature
