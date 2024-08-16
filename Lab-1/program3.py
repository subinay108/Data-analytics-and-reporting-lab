# WAPP to use response json() to print formatted string
import pprint
import requests

urlName = 'https://api.restful-api.dev/objects'

r = requests.get(urlName)

pprint.pprint(r.json())