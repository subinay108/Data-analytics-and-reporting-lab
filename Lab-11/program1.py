# Write a python code to generate a word cloud and find most important words and find frequency
from wordcloud import WordCloud
import matplotlib.pyplot as plt

file = open('transformer.txt', 'r')

text = file.read()

# print(text)

wc = WordCloud().generate(text)

plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()

word_frequencies = wc.words_

most_important_word = max(word_frequencies, key=word_frequencies.get)
print('Most Important Word: ', most_important_word)