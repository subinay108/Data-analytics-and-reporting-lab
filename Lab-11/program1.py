# Write a python code to generate a word cloud and find most important words and find frequency
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re
from collections import Counter

file = open('transformer.txt')

text = file.read()

text = re.sub(r'[,.]', '', text).lower()

# print(text)

wc = WordCloud().generate(text)

plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()

word_values = wc.words_

most_important_word = max(word_values, key=word_values.get)
print('Most Important Word: ', most_important_word)

word_frequencies = Counter(text.split())

print(word_frequencies)