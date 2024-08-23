# WAPP to find elements by class from a webpage
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://editorial.rottentomatoes.com/guide/popular-movies/')
bs = BeautifulSoup(html.read(), 'html.parser')

# print(bs.get_text())

content = bs.find_all(class_='article_movie_title')

for movies in content:
    print(movies.get_text())
