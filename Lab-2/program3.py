# WAPP to web scraping program to extract titles from a web page

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://en.wikipedia.org/wiki/List_of_computer_scientists')
bs = BeautifulSoup(html.read(), 'html.parser')

title = bs.find('title')
print(title.get_text())
