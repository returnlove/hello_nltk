import nltk
# nltk.download()
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.corpus import state_union

# example_text = "hello world!, welcome again to naturla language processing!. Lets refresh this!"
# print(sent_tokenize(example_text))
# print(word_tokenize(example_text))

# example_sent = "This is a sample sentence, showing off the stop words filtration."

# stop_words = set(stopwords.words('english'))
# word_tokens = word_tokenize(example_sent)
# filtered_words = [w for w in word_tokens if w not in stop_words ]
# print(word_tokens)
# print(filtered_words)

# example_words = ["talk", "talking","talked","talkings"]
# ps = PorterStemmer()

# for w in example_words:
# 	print(ps.stem(w))


# new_text = "It is important to by very pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once."
# ps = PorterStemmer()

# words = word_tokenize(new_text)
# # print(words)
# for w in words:
# 	print(ps.stem(w))


# new_text = "It is important to by very pythonly while you are pythoning with python."
# words = word_tokenize(new_text)
# # print(words)
# # for w in words:
# # 	print('the word is : ', w)
# # 	print(nltk.pos_tag(w))
# print(nltk.pos_tag(words))

sample_text = state_union.raw("2006-GWBush.txt")
words = word_tokenize(sample_text)
print(nltk.pos_tag(words[:5]))





