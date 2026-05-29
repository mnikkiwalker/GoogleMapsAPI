import config as cf
import maps_client




def getGeocode(address_block):
    client_config = cf.MapsAPIConfig.from_sources()
    client = maps_client.MapsClient(client_config)  

    address = f"{address_block.get("street")}, {address_block.get("city")} {address_block.get("state")}"
    postal_code = address_block.get("zip")

    print("Address: ", address, postal_code)

    response = client.geocode_address(address, postal_code)
    geocode = response["results"][0]["geometry"]["location"]

    return geocode