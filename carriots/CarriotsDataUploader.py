"""
CarriotsDataUploader class sends weather station data to Carriots IoT platform via REST API
"""

# *** IMPORTS *** #
import os
import urllib.request
import urllib.parse
import json
import time

# *** CONSTANTS *** #
CARRIOTS_API_URL = "CARRIOTS_API_URL"
CARRIOTS_API_KEY = "CARRIOTS_API_KEY"
CARRIOTS_API_DEVICE = "CARRIOTS_API_DEVICE"


# *** CLASS *** #
class CarriotsDataUploader(object):

    # *** API *** #
    def upload_data(self,
                    humidity,
                    temperature):

        data = dict(
            humidity=humidity,
            temperature=temperature
        )

        self._upload_data(data)

    def upload_humidity_data(self,
                             humidity):

        data = dict(
            humidity=humidity
        )

        self._upload_data(data)

    def upload_temperature_data(self,
                                temperature):

        data = dict(
            temperature=temperature
        )

        self._upload_data(data)

    # *** PRIVATE *** #
    def _upload_data(self, data):

        timestamp = self._get_timestamp()
        carriots_api_url = self._get_carriots_api_url()
        carriots_api_key = self._get_carriots_api_key()
        carriots_api_device = self.get_carriots_api_device()


        params = {
            "protocol": "v2",
            "device": carriots_api_device,
            "at": timestamp,
            "data": data
        }

        binary_data = json.dumps(params).encode("ascii")

        header = {
            "User-Agent": "raspberrycarriots",
            "Content-Type": "application/json",
            "carriots.apikey": carriots_api_key
        }

        req = urllib.request.Request(
            carriots_api_url,
            binary_data,
            header
        )

        res = urllib.request.urlopen(req)

        return res

    def _get_carriots_api_url(self):

        try:

            carriots_api_url = os.environ[CARRIOTS_API_URL]

            return carriots_api_url

        except KeyError as exc:
            print("Can't get Carriots environment variable to send data to cloud servers. Details = %s" % str(exc))
            raise

    def _get_carriots_api_key(self):

        try:

            carriots_api_key = os.environ[CARRIOTS_API_KEY]

            return carriots_api_key

        except KeyError as exc:
            print("Can't get Carriots environment variable to send data to cloud servers. Details = %s" % str(exc))
            raise


    def get_carriots_api_device(self):

        try:

            carriots_api_device = os.environ[CARRIOTS_API_DEVICE]

            return carriots_api_device

        except KeyError as exc:
            print("Can't get Carriots environment variable to send data to cloud servers. Details = %s" % str(exc))
            raise


    def _get_timestamp(self):
        return int(time.time())
