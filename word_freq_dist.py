import nltk

from nltk import FreqDist
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
#from nltk import word_tokenize

def word_frequency_distribution(texto,language):
    '''
    delete punctuation => tokenize => delete stopwords => FreqDist
    '''

    if language == 'es':
        language = "spanish"
    elif language == 'en':
        language = "english"

    '''
    esto parece que no tiene utilidad
    if self.language == "spanish":
        nltk.download('cess_esp')
        corpus = nltk.corpus.cess_esp.sents()
    elif self.language == "english":
    '''

    stopwd = stopwords.words(language)
    tokenizer = RegexpTokenizer(r'\w+')
    content = []
    texto = tokenizer.tokenize(texto) #elimina signos de puntuación y TOKENIZA

    for word in texto:
        if word.lower() not in stopwd:
            content.append(word.lower()) 
    texto = content #elimina stopwords
    distribucion = FreqDist(texto)
    return distribucion
