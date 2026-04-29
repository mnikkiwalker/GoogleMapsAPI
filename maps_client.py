from urllib import parse
import requests

class MapsClient:
    def __init__(self, config):
        self.config = config

    # def authenticate(self):

    #     print("Authentication initiated")
    #     print("-"*20)


    def geocode_address(self, address, postal_code):

        encoded_address = parse.quote_plus(address)
        url = self.config.api_base_url

        params = {
            "address": encoded_address,
            "components": f"postal_code: {postal_code}|country:US",
            "key": self.config.maps_api_key
        }

        response = requests.get(url, params=params)

        return response.json()



        