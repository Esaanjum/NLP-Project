# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 12:30:40 2023

@author: Esa
"""

import spacy
from spacy_wordnet.wordnet_annotator import WordnetAnnotator


class NLP_Search:
    """class for searching relevant text with Natural Language Processing."""
    
    # spacy english model
    nlp = spacy.load('en_core_web_lg')
    
    def __init__(self, search_input):
        """Initialise a nlp_search object.
        
        Parameters
        ----------
        search_input : str
        
        """
    
        self.search_input = search_input
        self.nlp.add_pipe("spacy_wordnet", after='tagger')
        self.doc = self.nlp(search_input)
        
        

    def find_synonyms(self):
        """Find synonyms of input in the text.
        
        RETURNS
        -------
        synonyms : list.
        
        """
        # find synonyms of only 1 word from input
        token = self.doc[0]
        synsets = token._.wordnet.synsets()
        lemmas = token._.wordnet.lemmas()
        synonyms = set()
        for lemma in lemmas:
            synonyms.add(lemma.name())
        
        return synonyms



