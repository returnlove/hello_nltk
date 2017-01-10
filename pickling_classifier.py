import nltk
import random
from nltk.corpus import movie_reviews
import pickle
import os

print(os.getcwd())

def main():

	# documents list will have the list of words and the category of the document (either pos or neg)
	documents = []

	for category in movie_reviews.categories():
		for fileid in movie_reviews.fileids(category):
			documents.append((list(movie_reviews.words(fileid)), category))

	# grab all the words in a variable		
	all_words = []

	for w in movie_reviews.words():
		all_words.append(w.lower())

	# frequency dist
	all_words = nltk.FreqDist(all_words)

	# considering the top 3000 words as word features
	word_features = list(all_words.keys())[:3000]
	# print(len(word_features))

	# function which will create words features for a given document. We have selected top 3000 words as features according to the freq dist
	# for these 300 features we will get true or false according to their presence in the document
	def find_features(document):
		words = set(document)
		features = {}
		for w in word_features:
			features[w] = (w in words)
		return features

	# print(len((find_features(movie_reviews.words('neg/cv000_29416.txt')))))
	# print((find_features(movie_reviews.words('pos/cv014_13924.txt'))))

	# for each document it extracts the word features (wheather true or false along with the lablel i.e. pos or neg)
	featuresets = [(find_features(rev), category) for (rev, category) in documents]

	# print(featuresets[:1][0])
	# test = featuresets[:1][0]
	# test = test[0]
	# print(len(test))
	# for e in featuresets[:1][0
	# 	print(e)

	# test = [cat for (rev, cat) in documents]
	# my_dict = {}

	# for ele in test:
	# 	if ele not in my_dict.keys():
	# 		my_dict[ele] = 1
	# 	elif ele in my_dict.keys():
	# 		my_dict[ele] += 1

	# print(my_dict)

	# print(featuresets[0])

	training_set = featuresets[:1900]

	testing_set = featuresets[1900:]

	clf = nltk.NaiveBayesClassifier.train(training_set)
	# print("Classifier test percentage: ", (nltk.classify.accuracy(clf, testing_set))*100)

	# clf.show_most_informative_features(15)

	save_clf = open("naivbayes.pickle", "wb")
	pickle.dump(clf, save_clf)
	save_clf.close()

	print(os.path.abspath("naivbayes.pickle"))


	clf_f = open("naivbayes.pickle", "rb")
	clf = pickle.load(clf_f)
	clf_f.close()

if __name__ == "__main__":
	main()
