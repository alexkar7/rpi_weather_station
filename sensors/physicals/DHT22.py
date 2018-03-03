# *** IMPORTS *** #
import Adafruit_DHT


# *** CLASS *** #
class DHT22(object):
    
    sensor = Adafruit_DHT.DHT22
    
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
            humidity, temperature = Adafruit_DHT.read_retry(DHT22.sensor, self.gpio_pin)

        return humidity

    """
    Get current temperature
    """
    def get_temperature(self):

        temperature = None

        while temperature is None:
            humidity, temperature = Adafruit_DHT.read_retry(DHT22.sensor, self.gpio_pin)

        return temperature
