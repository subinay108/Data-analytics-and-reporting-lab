# WAPP to Implement API Request using Get

import requests

urlName = 'https://en.wikipedia.org/wiki/Deadpool_%26_Wolverine'

response = requests.get(urlName)

print(response.status_code)