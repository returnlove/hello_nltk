'''
A very similar operation to stemming is called lemmatizing. 
The major difference between these is, as you saw earlier, stemming can often create non-existent words, 
whereas lemmas are actual words.
'''


from nltk.stem import WordNetLemmatizer


def main():
	lemmatizer = WordNetLemmatizer()
	print(lemmatizer.lemmatize("shoes"))
	print(lemmatizer.lemmatize("shirts"))
	print(lemmatizer.lemmatize("appreciating"))
	# print(lemmatizer.lemmatize("lovely", pos = "a"))
	print(lemmatizer.lemmatize("better"))
	# defaut pos is noun where it will find closest noun. We can pass the suitable pos
	print(lemmatizer.lemmatize("better", pos = "a"))


if __name__ == "__main__":
	main()