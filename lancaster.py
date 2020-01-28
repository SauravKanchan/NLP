# import nltk

# nltk.download('punkt')
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import *

for line in open("para.txt","r"):
    print("Line is ",line)
    for sent in sent_tokenize(line):
        words = word_tokenize(sent)
        stemmer = LancasterStemmer()
        for w in words:
            print("Word is {0} and it's stem is {1}".format(w, stemmer.stem(w)))