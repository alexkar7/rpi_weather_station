"""
Main project class. This class controls all the behaviour for my weather station
"""
# *** IMPORTS *** #
from sensors import temperature_sensor
from sensors import humidity_sensor
from carriots import carriots_data_uploader


# *** CLASS *** #
class WeatherStationManager(object):

    # *** API *** #
    def upload_data_2_carriots(self):

        temperature = temperature_sensor.get_temperature()
        humidity = humidity_sensor.get_humidity()

        carriots_response = carriots_data_uploader.upload_data(
            temperature=temperature,
            humidity=humidity)

        print("carriots response code = " + carriots_response.status_code)
