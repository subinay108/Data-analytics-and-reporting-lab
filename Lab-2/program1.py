# WAPP to requests making get request
import requests

# urlName = input('Enter the url: ')
urlName = 'https://www.google.com'
response = requests.get(urlName)

print(response.text)