from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from word import Word
from review import Review
from collections import Counter
import csv
import re

NUM_PROP = 14

def main():
    parseCSV("example2.csv")

    # parseCSV("example2.csv")
    # print("STEMMER: ", stem[1], "\n\n")
    # print("LEMMATIZER: ", lemma[1])

def scoreReview(db, review):
    reviewScores = [0]*NUM_PROP
    wordCount = Counter(reduceReview(review))

    for word, count in wordCount.items():
        wordScores = db[word.upper()]
        reviewScores[0] += wordScores.nlet*count
        reviewScores[1] += wordScores.nphon*count
        reviewScores[2] += wordScores.nsyl*count
        reviewScores[3] += wordScores.kffreq*count
        reviewScores[4] += wordScores.kfcats*count
        reviewScores[5] += wordScores.kfsamps*count
        reviewScores[6] += wordScores.tlfreq*count
        reviewScores[7] += wordScores.bfreq*count
        reviewScores[8] += wordScores.fam*count
        reviewScores[9] += wordScores.conc*count
        reviewScores[10] += wordScores.imag*count
        reviewScores[11] += wordScores.meanc*count
        reviewScores[12] += wordScores.meanp*count
        reviewScores[13] += wordScores.aoa*count

    return reviewScores

def parseCSV(fileName):
    print("working...")
    reviews = []
    listReview = []
    listLemma = []
    db = buildMRC("1054/mrc2.dct")
    newCols = ["NLET", "NPHON", "NSYL", "KFFREQ", "KFCATS", "KFSAMPS", "TLFREQ",
        "BFREQ", "FAM", "CONC", "IMAG", "MEANC", "MEANP", "AOA"]
    with open(fileName, 'r') as csvInput:
        with open("out.csv", 'w') as csvOutput:
            reader = csv.reader(csvInput, delimiter=',', quotechar='"')
            writer = csv.writer(csvOutput, delimiter=',', quotechar='"')
            row0 = next(reader)
            row0.extend(newCols)
            writer.writerow(row0)
            for row in reader:
                review = reduceReview(row[9])
                reviewScores = scoreReview(db, review)
                row.extend(reviewScores)
                writer.writerow(row)
    print("...done")

# USE THIS ONE
# def parseCSV(fileName):
#     reviews = []
#     listLemma = []
#     words = buildMRC("1054/mrc2.dct")
#     with open(fileName, newline='') as csvInput:
#         reader = csv.reader(csvInput, delimiter=',', quotechar='"')
#         for row in reader:
#             scoreReview(words, row[9])


# def reduceReview(reviewStr):
#     #Initializing necessary lists + stemmers for use later
#     stopWords = set(stopwords.words('english'))
#     sno = SnowballStemmer('english')
#     lmtzr = WordNetLemmatizer()
#
#     wordList = re.sub("[^\w&^']", " ", reviewStr).split()
#     finalList = [sno.stem(word) for word in wordList if word not in stopWords]
#     lemmaList = [lmtzr.lemmatize(word) for word in wordList if word not in stopWords]
#     return finalList, lemmaList


def reduceReview(reviewStr):
    #Initializing necessary lists + stemmers for use later
    stopWords = set(stopwords.words('english'))
    lmtzr = WordNetLemmatizer()
    wordList = re.sub("[^\w&^']", " ", reviewStr).split()
    lemmaList = [lmtzr.lemmatize(word) for word in wordList if word not in stopWords]
    return lemmaList

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

if __name__ == "__main__":
    main()
