from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords, wordnet
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import pos_tag
from word import Word
from review import Review
from collections import Counter
import csv
import re
import os

NUM_PROP = 14

def main():
    parseCSV("amazon_cr_100Ksample.csv")


def reduceReview(reviewStr):
    #Initializing necessary lists + stemmers for use later
    stopWords = set(stopwords.words('english'))
    lmtzr = WordNetLemmatizer()
    result = []
    originalNoPunc = re.sub("[^\w&^']", " ", reviewStr).split()
    finalList = [ word.lower() for word in originalNoPunc if word.lower() not in
        stopWords and not isNumber(word)]
    taggedWords = pos_tag(finalList)

    for wordPair in taggedWords:
        word = wordPair[0]
        tag = wordPair[1]
        newTag = convertTag(tag)
        result.append(lmtzr.lemmatize(word, newTag))
    return result

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


def scoreReview(db, review):
    reviewScores = [0]*(NUM_PROP*3 + 1)
    wordCount = Counter(reduceReview(review))

    for word, count in wordCount.items():
        wordScores = db.get(word.upper())
        reviewScores[0] += count #Total word count after stemming

        if(wordScores is not None):
            reviewScores[1] = reviewScores[1]+count if wordScores.nlet != 0 else reviewScores[1]
            reviewScores[2] += wordScores.nlet*count

            reviewScores[4] = reviewScores[4]+count if wordScores.nphon != 0 else reviewScores[4]
            reviewScores[5] += wordScores.nphon*count

            reviewScores[7] = reviewScores[7]+count if wordScores.nsyl != 0 else reviewScores[7]
            reviewScores[8] += wordScores.nsyl*count

            reviewScores[10] = reviewScores[10]+count if wordScores.kffreq != 0 else reviewScores[10]
            reviewScores[11] += wordScores.kffreq*count

            reviewScores[13] = reviewScores[13]+count if wordScores.kfcats != 0 else reviewScores[13]
            reviewScores[14] += wordScores.kfcats*count

            reviewScores[16] = reviewScores[16]+count if wordScores.kfsamps != 0 else reviewScores[16]
            reviewScores[17] += wordScores.kfsamps*count

            reviewScores[19] = reviewScores[19]+count if wordScores.tlfreq != 0 else reviewScores[19]
            reviewScores[20] += wordScores.tlfreq*count

            reviewScores[22] = reviewScores[22]+count if wordScores.bfreq != 0 else reviewScores[22]
            reviewScores[23] += wordScores.bfreq*count

            reviewScores[25] = reviewScores[25]+count if wordScores.fam != 0 else reviewScores[25]
            reviewScores[26] += wordScores.fam*count

            reviewScores[28] = reviewScores[28]+count if wordScores.conc != 0 else reviewScores[28]
            reviewScores[29] += wordScores.conc*count

            reviewScores[31] = reviewScores[31]+count if wordScores.imag != 0 else reviewScores[31]
            reviewScores[32] += wordScores.imag*count

            reviewScores[34] = reviewScores[34]+count if wordScores.meanc != 0 else reviewScores[34]
            reviewScores[35] += wordScores.meanc*count

            reviewScores[37] = reviewScores[37]+count if wordScores.meanp != 0 else reviewScores[37]
            reviewScores[38] += wordScores.meanp*count

            reviewScores[40] = reviewScores[40]+count if wordScores.aoa != 0 else reviewScores[40]
            reviewScores[41] += wordScores.aoa*count

    finalScores = insertAverages(reviewScores)
    return finalScores

def insertAverages(reviewScores):
    for i in range(1, 15):
        j = i*3
        count = reviewScores[j-2]
        total = reviewScores[j-1]
        reviewScores[j] = round(total/count,3) if count != 0 else 0
    return reviewScores


def parseCSV(fileName):
    print("working...")
    reviews = []
    listReview = []
    listLemma = []
    db = buildMRC("1054/mrc2.dct")
    newCols = ["Word count", "numNLET", "sumNLET", "avgNLET", "numNPHON",
        "sumNPHON", "avgNPHON", "numNSYL", "sumNSYL", "avgNSYL", "numKFFREQ",
        "sumKFFREQ", "avgKFFREQ", "numKFCATS", "sumKFCATS", "avgKFCATS",
        "numKFSAMPS", "sumKFSAMPS", "avgKFSAMPS", "numTLFREQ", "sumTLFREQ",
        "avgTLFREQ", "numBFREQ", "sumBFREQ", "avgBFREQ", "numFAM", "sumFAM",
        "avgFAM", "numCONC", "sumCONC", "avgCONC", "numIMAG", "sumIMAG",
        "avgIMAG", "numMEANC", "sumMEANC", "avgMEANC", "numMEANP", "sumMEANP",
        "avgMEANP", "numAOA", "sumAOA", "avgAOA"]
    with open(fileName, 'r', encoding="ISO-8859-1") as csvInput:
        with open("out.csv", 'w', encoding="ISO-8859-1") as csvOutput:
            reader = csv.reader(csvInput, delimiter=',', quotechar='"')
            writer = csv.writer(csvOutput, delimiter=',', quotechar='"')
            row0 = next(reader)
            row0.extend(newCols)
            writer.writerow(row0)
            for row in reader:
                review = row[9]
                reviewScores = scoreReview(db, review)
                row.extend(reviewScores)
                writer.writerow(row)
    print("...done")

def buildMRC(fileName):
    words = {}
    with open(fileName) as f:
        lines = f.read().splitlines()
    for i in range(0, len(lines)):
        line = lines[i]
        numScores = 0
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
        scores = [nlet, nphon, nsyl, kffreq, kfcats, kfsamps, tlfreq, bfreq, fam,
            conc, imag, meanc, meanp, aoa]
        #Count the number of non-zero scores for this entry
        for score in scores:
            if score != 0:
                numScores += 1
        word = extractWord(lines[i])
        newWord = Word(nlet, nphon, nsyl, kffreq, kfcats, kfsamps,
            tlfreq, bfreq, fam, conc, imag, meanc, meanp, aoa, numScores)

        #Get the current entry in our DB for this word. If the word already
        #exists in our DB, then compare the number of scores on record to our newWord
        #If the newWord has more entries, it is considered to be more "complete"
        #and therefore will replace the current entry
        currentWord = words.get(word)
        if(currentWord is not None):
            if(currentWord.numScores < newWord.numScores):
                words[word] = newWord
        else:
            words[word] = newWord
    return words

def isNumber(str):
    try:
        float(str)
        return True
    except:
        return False

def extractWord(line):
    index = 51
    while line[index] != '|':
        index += 1
    return line[51:index]

if __name__ == "__main__":
    main()
