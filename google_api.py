
import requests
import urllib.parse

address = '8 Williams Drive, Hounslow TW3 3RG'
url = f'https://nominatim.openstreetmap.org/search/{urllib.parse.quote(address)}?format=json'

response = requests.get(url).json()
print(response)
print(response[0]["lat"])
print(response[0]["lon"])