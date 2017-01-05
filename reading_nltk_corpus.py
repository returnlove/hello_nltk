from nltk.corpus import product_reviews_1
from nltk.tokenize import sent_tokenize

def main():
	text = product_reviews_1.raw("Canon_G3.txt")
	# print(text[:1000])
	tokenized = sent_tokenize(text)
	for i in range(10):
		print(tokenized[i])


if __name__ == "__main__":
	main()