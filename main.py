import maps_client
import config


client_config = config.MapsAPIConfig.from_sources()
client = maps_client.MapsClient(client_config)

test_params = {
    "street": "2799 Bay Dr",
    "city": "West Bloomfield",
    "state": "MI",
    "zip": 48324
}

address = f"{test_params.get("street")}, {test_params.get("city")} {test_params.get("state")}"
postal_code = test_params.get("zip")


response = client.geocode_address(address, postal_code)
print(response)