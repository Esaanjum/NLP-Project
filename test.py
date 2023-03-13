# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 10:06:41 2023

@author: Esa
"""

import spacy
from spacy.matcher import Matcher
nlp = spacy.load('en_core_web_lg')


search_txt = 'vanished'
long_txt_doc = nlp('I am vanishing great. How do you do?')
search_txt_doc = nlp(search_txt)
forms_of_verbs = set()
for token in long_txt_doc:
    print(type(token))
    if token.lemma_ == search_txt_doc[0].lemma_ and token.pos_==search_txt_doc[0].pos_:
        forms_of_verbs.add(token.text)



