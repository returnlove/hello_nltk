import nltk
from nltk.corpus import state_union
from nltk.tokenize import sent_tokenize, word_tokenize

# def process_content():
# 	text = state_union.raw("2006-GWBush.txt")
# 	# print(text)

# 	sent_tokenized = sent_tokenize(text)
# 	# print(sent_tokenized[:2])

# 	for sent in sent_tokenized[:10]:
# 		words = nltk.word_tokenize(sent)
# 		tagged = nltk.pos_tag(words)
# 		namedEnt = nltk.ne_chunk(tagged, binary = True)
# 		namedEnt.draw()

def process_content():
	text = state_union.raw("2006-GWBush.txt")
	# text = "george bush was president of the America and he born in the month of January"
	# print(text)	
	words = word_tokenize(text)
	words = words[:500]
	tagged = nltk.pos_tag(words)
	namedEnt = nltk.ne_chunk(tagged, binary = True)
	# namedEnt = nltk.ne_chunk(tagged)

	print(namedEnt)
	# namedEnt.draw()

def print_text():
	text = state_union.raw("2006-GWBush.txt")
	print(text)

def main():
	# process_content()
	print_text()

if __name__ == "__main__":
	main()

