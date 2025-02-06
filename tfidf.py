import math

MIN_WORD_OCCURENCE = 3

def create_word_table(splitTexts : list[list[str]]):
    words = count_words(splitTexts)
    voc = {}
    i = 0
    for word in words:
        if words[word] >= MIN_WORD_OCCURENCE:
            voc[word] = i 
            i += 1
    return voc

def count_words(splitTexts : list[list[str]]):
    wordcount = {}
    for splitText in splitTexts:
        for word in splitText:
            if word not in wordcount:
                wordcount[word] = 1 
            else :
                wordcount[word] += 1
    return wordcount

def vectorize_text(splitText : list[str], wordTable : dict):
    vector = [0] * len(wordTable)
    for word in splitText:
        if(word in wordTable):
            vector[wordTable[word]] += 1

def vectorize_text_bin(splitText : list[str], wordTable : dict):
    vector = [0] * len(wordTable)
    for word in splitText:
        if(word in wordTable):
            vector[wordTable[word]] = 1

def count_word_in_text(splitText : list[str], wordToCount : str): 
    i = 0
    for word in splitText:
        if word == wordToCount:
            i += 1
    return i

def count_doc_including_word(splitTexts: list[list[str]], word : str):
    i = 0
    for splitText in splitTexts:
        if word in splitText:
            i += 1
    return i

def term_freq(splitText : list[str], word : str):
    return count_word_in_text(splitText, word) / len (splitText)

def inverse_freq(splitTexts : list[list[str]], word :str):
    k = len(splitTexts)

    return math.log(k / count_doc_including_word(splitTexts, word))

def tfidf(splitTexts : list[list[str]], splitText : list[str], word :str):
    return term_freq(splitText, word) * inverse_freq(splitTexts, word)

def vectorize_text_tfidf(splitTexts : list[list[str]], splitText : list[str], wordTable :dict):
    tfidfVect = [0] * len(wordTable)
    i = 0
    for word in wordTable:
        tfidfVect[i] = tfidf(splitTexts, splitText, word)
        i += 1
    return tfidfVect


