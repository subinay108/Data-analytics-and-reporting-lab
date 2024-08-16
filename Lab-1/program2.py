# WAPP to use response json() using Request

import requests

urlName = 'https://api.restful-api.dev/objects'

r = requests.get(urlName)

print(r.json())