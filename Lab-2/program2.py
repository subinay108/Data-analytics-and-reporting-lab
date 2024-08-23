# WAPP to parsing the HTML using beautifulsoup
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://en.wikipedia.org/wiki/List_of_computer_scientists')
bs = BeautifulSoup(html.read(), 'html.parser')

content = bs.find('div', {'id': 'bodyContent'})
scientistList = content.find_all('li');
for scientist in scientistList:
    print(scientist.get_text())
