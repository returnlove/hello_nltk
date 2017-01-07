

import nltk
import random
from nltk.corpus import movie_reviews


# print(movie_reviews.categories())
# print(dir(movie_reviews))
# print(movie_reviews.fileids('neg'))

# documents_1 = [(list(movie_reviews.words(fileid)), category) for category in movie_reviews.categories() for fileid in movie_reviews.fileids(category)]
# print(documents)
# print(len(documents_1))

documents = []

for category in movie_reviews.categories():
	for fileid in movie_reviews.fileids(category):
		documents.append((list(movie_reviews.words(fileid)), category))

# print(len(documents))
print(documents[:1])
# random.shuffle(documents)
print(documents[:1])


all_words = []

for w in movie_reviews.words():
	all_words.append(w.lower())

print(len(all_words))