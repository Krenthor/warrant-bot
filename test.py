from geopandas
from geopy

locator = Nominatim(user_agent=”myGeocoder”)
location = locator.geocode(“Champ de Mars, Paris, France”)

print(“Latitude = {}, Longitude = {}”.format(location.latitude, location.longitude))

