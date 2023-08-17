######################## INITIAL IMPORTS #######################

import unicodedata
import re
import json

import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords

import pandas as pd
import acquire
from time import strftime

import warnings
warnings.filterwarnings('ignore')


###################### BASIC CLEAN FUNCTION ######################

def basic_clean(string):
    """
    This function puts a string in lowercase, normalizes any unicode characters,
    Removes anything that isn't an alphanumeric symbol or single quote.
    """
    # Normalize unicode characters
    string = unicodedata.normalize('NFKD', string)\
    .encode('ascii', 'ignore')\
    .decode('utf-8', 'ignore')
    
    # Remove unwanted characters and put string in lowercase
    string = re.sub(r"[^\w0-9'\s]", '', string).lower()
            
    return string


##################### TOKENIZE FUNCTION ##########################

def tokenize(string):
    """
    Takes in a string and tokenizes it. Returns the tokenized string.
    """
    # Build the tokenizer
    tokenizer = nltk.tokenize.ToktokTokenizer()
    
    # Tokenize the string with the tok-tok-tokenizerrr
    string = tokenizer.tokenize(string, return_str = True)
    
    return string


###################### STEM FUNCTION ############################

def stem(string):
    """
    This function takes in a string, stems it, and returns a stemmed version of the original string
    """
    # Build the stemmer
    stemmer = nltk.porter.PorterStemmer()
    
    # Use the stemmer on each word in the string and append to the results list
    results = []
    for word in string.split():
        results.append(stemmer.stem(word))
        
    # Convert back into a string
    string = ' '.join(results)
    
    return string


##################### LEMMATIZE FUNCTION #########################

def lemmatize(string):
    """
    This function takes in a string, lemmatizes each word, and returns a lemmatized version of the orignal string
    """
    # Build the lemmatizer
    lemmatizer = nltk.stem.WordNetLemmatizer()
    
    results = []
    for word in string.split():
        results.append(lemmatizer.lemmatize(word))
    
    # Convert back into a string
    string = ' '.join(results)

    return string


######################## REMOVE STOPWORDS FUNCTION ###########################

def remove_stopwords(string, extra_words=None, exclude_words=None):
    '''
    Takes in a string, with optional arguments for words to add to stock stopwords and words to ignore in the stock list
    removes the stopwords, and returns a stopword free version of the original string
    '''
    # Get the list of stopwords from nltk
    stopword_list = stopwords.words('english')
    
    # Create a set of stopwords to exclude
    excluded_stopwords = set(exclude_words) if exclude_words else set()
    
    # Include any extra words in the stopwords to exclude
    stopwords_to_exclude = set(stopword_list) - excluded_stopwords
    
    # Add extra words to the stopwords set
    stopwords_to_exclude |= set(extra_words) if extra_words else set()
    
    # Tokenize the input string
    words = string.split()
    
    # Filter out stopwords from the tokenized words
    filtered_words = [word for word in words if word not in stopwords_to_exclude]
    
    # Convert back to string
    string = ' '.join(filtered_words)
    
    return string