

import nltk
import random
from nltk.corpus import movie_reviews

documents = []

for category in movie_reviews.categories():
	for fileid in movie_reviews.fileids(category):
		documents.append((list(movie_reviews.words(fileid)), category))


all_words = []

for w in movie_reviews.words():
	all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)

# print(all_words.most_common(10))

# print(all_words['stupid'])

word_features = list(all_words.keys())[:3000]

# print(word_features)

# print(set(movie_reviews.words('neg/cv000_29416.txt')))

def find_features(document):
	words = set(document)
	features = {}
	for w in word_features:
		features[w] = (w in words)
	return features
print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))
