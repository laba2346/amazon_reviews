from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from word import Word
import csv
import re

def parseCSV(fileName):
    reviews = []
    listReview = []
    listLemma = []

    with open(fileName, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            reviews.append(row[9])
    for review in reviews:
        sno,lemma = reduceReview(review)
        listReview.append(sno)
        listLemma.append(lemma)



    return listReview,listLemma

def reduceReview(reviewStr):
    #Initializing necessary lists + stemmers for use later
    stopWords = set(stopwords.words('english'))
    sno = SnowballStemmer('english')
    lmtzr = WordNetLemmatizer()

    wordList = re.sub("[^\w&^']", " ", reviewStr).split()
    finalList = [sno.stem(word) for word in wordList if word not in stopWords]
    lemmaList = [lmtzr.lemmatize(word) for word in wordList if word not in stopWords]
    return finalList, lemmaList

def buildMRC(fileName):
    words = {}
    with open(fileName) as f:
        lines = f.read().splitlines()
    for i in range(0, len(lines)):
        line = lines[i]
        nlet = int(line[0:2])
        nphon = int(line[2:4])
        nsyl = int(line[4])
        kffreq = int(line[5:10])
        kfcats = int(line[10:12])
        kfsamps = int(line[12:15])
        tlfreq = int(line[15:21])
        bfreq = int(line[21:25])
        fam = int(line[25:28])
        conc = int(line[28:31])
        imag = int(line[31:34])
        meanc = int(line[34:37])
        meanp = int(line[37:40])
        aoa = int(line[40:43])
        word = extractWord(lines[i])
        newWord = Word(nlet, nphon, nsyl, kffreq, kfcats, kfsamps,
            tlfreq, bfreq, fam, conc, imag, meanc, meanp, aoa)
        words[word] = newWord
    return words

def extractWord(line):
    index = 51
    while line[index] != '|':
        index += 1
    return line[51:index]

# #words = buildMRC("1054/mrc2.dct")
# word = "ZOOM"
# print('ZOOM: ')
# words[word].printAll()
