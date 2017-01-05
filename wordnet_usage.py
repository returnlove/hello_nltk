from nltk.corpus import wordnet

def syn_antonym():
	synonyms = []
	antonyms = []

	# print(wordnet.synsets("good")[0].lemmas()[0].antonyms())
	for syn in wordnet.synsets("good"):
		for l in syn.lemmas():
			synonyms.append(l.name())
			if l.antonyms():
				antonyms.append(l.antonyms()[0].name())
	print(set(synonyms))
	print(set(antonyms))	


def check_similarity(word1, word2):
	w1 = wordnet.synset(word1)
	w2 = wordnet.synset(word2)
	print(w1.wup_similarity(w2))

def main():
	# syn_antonym()
	check_similarity('love.n.01', 'cat.n.01')
	check_similarity('love.n.01', 'love.n.01')
			

if __name__ == "__main__":
	main()
