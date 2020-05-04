"""
Code taken from Ng Wai Foong's tutorial at:
https://medium.com/better-programming/extract-keywords-using-spacy-in-python-4a8415478fbf"""

import spacy
from collections import Counter
from string import punctuation

nlp = spacy.load("en_core_web_sm")


def get_keywords(text):
    result = []
    pos_tag = ['PROPN', 'ADJ', 'NOUN']
    doc = nlp(text.lower())
    for token in doc:
        if(token.text in nlp.Defaults.stop_words or token.text in punctuation):
            continue
        if(token.pos_ in pos_tag):
            result.append(token.text)
    try:
        return Counter(result).most_common(1)[0][0]  # return most common value
    except IndexError:
        return "null"
