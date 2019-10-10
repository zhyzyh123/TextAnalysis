"""main.py

Code scaffolding

"""

import os
import nltk
from nltk.corpus import brown
from nltk.corpus import wordnet as wn
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.text import Text
from nltk import numpy


def read_text(path): 
    if os.path.isfile(path)==True:
        raw=open(path,"r").read()
        tokens=nltk.word_tokenize(raw)
        text = Text(tokens)
        return text
    elif os.path.isdir(path)==True:
        filelists = PlaintextCorpusReader(path, '.*') 
        tokens = filelists.words()
        text = Text(tokens)
        return text
    else: print('Nothing Found') 


def token_count(text):
    return len(text)


def type_count(text):
    return len(set([w.lower() for w in text]))


def sentence_count(text):
    stop_punctuation = ['.','!','?','......','."']
    return sum([text.count(i) for i in stop_punctuation])



def most_frequent_content_words(text):
    punctuation = [',','.','--',"''",';','``','!',"'s",'?','-s','-ly','</s>','......','/']
    stopwords=nltk.corpus.stopwords.words('english')
    content = [w for w in text if w.lower() not in stopwords and w not in punctuation]
    fd = FreqDist(content)
    word_25= fd.most_common(25)
    return word_25


def most_frequent_bigrams(text):
    punctuation = [',','.','--',"''",';','``','!',"'s",'?','-s','-ly','</s>','......','/']
    stopwords=nltk.corpus.stopwords.words('english')
    content = [w for w in text if w.lower() not in stopwords and w not in punctuation]
    bi = list(nltk.bigrams(content))
    return FreqDist(bi).most_common(25)


class Vocabulary():

    def __init__(self, text):
        self.text = text
        pass

    def frequency(self, word):
        return text.count(word)

    def pos(self, word):
        word_tag = nltk.pos_tag([word])
        return word_tag[0][1][1].lower()

    def gloss(self, word):
        syn = wn.synsets(word)  
        return syn[0].definition()

    def quick(self, word):
        return sel.text.concordance(word)
        


categories = ('adventure', 'fiction', 'government', 'humor', 'news')


def compare_to_brown(text):
    punctuation = [',','.','--',"''",';','``','!',"'s",'?']
    stopwords=nltk.corpus.stopwords.words('english')
    content = [w for w in text if w.lower() not in stopwords and w not in punctuation]
    for c in categories:
        brown_copy = [w for w in brown.words(categories=c) if w not in stopwords]
        all_items = set(content).union(set(brown_copy))
        v1 = {m:0 for m in all_items}
        v2 = {m:0 for m in all_items}
        for w in content:
            v1[w] += 1
        for w in brown_copy:
            v2[w] += 1
        v1 = list(v1.values())
        v2 = list(v2.values())
        cos_similarity = numpy.dot(v1, v2)/(math.sqrt(numpy.dot(v1, v1)) * math.sqrt(numpy.dot(v2, v2)))
        print(c, round(cos_similarity,2))



if __name__ == '__main__':

    text = read_text('data/grail.txt')
    token_count(text)
