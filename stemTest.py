from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords, wordnet
from nltk.stem.wordnet import WordNetLemmatizer
from main import reduceReview

import nltk
import re
lmtzr = WordNetLemmatizer()
print(lmtzr.lemmatize("enjoyed"))
print(lmtzr.lemmatize("enjoyed", wordnet.VERB))

print(lmtzr.lemmatize("looks"))
stopWords = set(stopwords.words('english'))

print(lmtzr.lemmatize("using", wordnet.VERB))


def convertTag(tag):
    if tag.startswith("J"):
        return wordnet.ADJ
    elif tag.startswith("N"):
        return wordnet.NOUN
    elif tag.startswith("V"):
        return wordnet.VERB
    elif tag.startswith("R"):
        return wordnet.ADV
    else:
        return wordnet.NOUN

original = "The hose attachment has GOING to be placed on when you want to use it and my bare floor tool was missing. Looks nice and the floor options seems to work ok."
originalNoPunc = re.sub("[^\w&^']", " ", original).split()
finalStr = [word.lower() for word in originalNoPunc if word.lower() not in stopWords]
taggedWords = nltk.pos_tag(finalStr)
final = []
for wordPair in taggedWords:
    word = wordPair[0]
    tag = wordPair[1]
    final.append(lmtzr.lemmatize(word, convertTag(tag)))
    print(tag)
print("BEFORE: {} \n\n AFTER: {}".format(reduceReview(original), final))
