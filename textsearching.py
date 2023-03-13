# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 12:30:40 2023

@author: Esa
"""

import spacy
from spacy.matcher import Matcher
from spacy_wordnet.wordnet_annotator import WordnetAnnotator
from num2words import num2words
from word2number import w2n
import PyPDF2


class Relevant_Text:
    """class for finding all the text relevant in input search and the file
    with Natural Language Processing."""
    
    # spacy english model
    nlp = spacy.load('en_core_web_lg')
    nlp.add_pipe("spacy_wordnet", after='tagger')
    
    # matcher = Matcher(nlp.vocab)
    # # pattern for roman numbers
    # pattern = [{'REGEX':r'''^M{0,3}(CM|CD|D?C{0,3})?(XC|XL|L?X{0,3})?
    #             (IX|IV|V?I{0,3})?$'''}]
    # matcher.add("ROMAN_NUM", [pattern])
    
    def __init__(self, input_search, file_path):
        """Initialise a relevant_text object.
        
        Parameters
        ----------
        input_search (str) : input text to be searched.
        file_path (str) : path of the file for searching text.
        """
    
        self.input_search = input_search
        self.doc = self.nlp(input_search)
        self.found_relevant_text = []
        self.token = self.doc[0]
        self.file_txt = ''
        
        
    def read_txt_from_file():
  
        # creating a pdf file object
        pdfFileObj = open('example.pdf', 'rb')
          
        # creating a pdf reader object
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
          
        # printing number of pages in pdf file
        print(pdfReader.numPages)
          
        # creating a page object
        pageObj = pdfReader.getPage(0)
          
        # extracting text from page
        print(pageObj.extractText())
          
        # closing the pdf file object
        pdfFileObj.close()
        
        return pageObj.extractText()
        
        
    def find_relevant_text(self):
        """Find relevant text by executing appropriate function
        based on part of speech tag."""
        
        
        if self.token.pos_ == 'NUM':
            print(self.token.pos_)
            self.found_relevant_text.extend(self.get_numbers())
        
        elif self.token.pos_ in ['ADJ','INTJ']:
            print(self.token.pos_)
            self.found_relevant_text.extend(self.get_synonyms())
            
        elif self.token.pos_ == 'VERB':
            print(self.token.pos_)
            self.found_relevant_text.extend(self.get_lemma())
            
        print(self.found_relevant_text)


    def get_synonyms(self):
        """Get synonyms of a word in the text.
        
        Parameters
        ----------
        token(spacy.tokens.Token).
        
        Returns
        -------
        synonyms(list).

        """
        
        synsets = self.token._.wordnet.synsets()
        lemmas = self.token._.wordnet.lemmas()
        synonyms = set()
        for lemma in lemmas:
            synonyms.add(lemma.name())
        
        return synonyms
    
    
    def get_numbers(self):
        """Get expression of numbers in different forms.
        
        Uses doc object of the instance.
        
        Returns
        -------
        nums(list) : list of str.
        
        """
        
        # if the first number is a digit, convert all of the numbers to words
        if self.doc[0].text[0].isdigit():
            # remove commas first..
            txt = self.remove_commas()
            nums = self.convert_nums_to_words(txt)
            
        # else convert all of the words to numbers
        else:
            # replace punctuations first..
            txt = self.replace_punct_with_spaces()
            nums = self.convert_words_to_nums(txt)
            
        return nums
        
        
    def convert_nums_to_words(self, nums):
        """Convert numbers to words in multiple formats i.e. 
        cardinal & year.
        
        Parameters
        ----------
        nums(str).
        
        Returns
        -------
        nums_in_words(list) : list of str.
        
        """
        
        nums_in_words = []
        nums_in_words.append([num2words(nums,to='cardinal')])
        nums_in_words.append([num2words(nums,to='year')])
        
        return nums_in_words
    
    
    def convert_words_to_nums(self, nums_in_words):
        """Convert words to num.
        
        Parameters
        ----------
        nums_in_words(str)
        
        Returns
        -------
        (list) : list of str
        
        """
        
        return [str(w2n.word_to_num(nums_in_words))]
        
    
    def get_lemma(self):
        """Get lemma of the token.
        
        Parameters
        ----------
        token(spacy.tokens.token.Token)
        
        Returns
        -------
        doc(spacy.tokens.Doc)
        
        """
        return self.nlp(self.token.lemma_)
    
    
    def replace_punct_with_spaces(self)->str:
       """Return a string with punctuations replaced with spaces.
       
       Uses doc object of the instance.
       
       Returns
       -------
       txt (str)
       
       """ 
       
       txt = self.doc.text
       txt = list(txt)
       for token in self.doc:
           if token.is_punct:
               txt[token.idx] = ' '
       txt = ''.join(txt)
       
       return txt
    
    
    def remove_commas(self)->str:
        """Return a string with commas removed.
        
        Uses doc object of the instance.
        
        Returns
        -------
        txt (str)
        
        """
        
        txt = self.doc.text
        txt = txt.replace(',', '')
        
        return txt
        

# class NLP_Search(Related_Text):
#     """class for highlighting relevant text in a document."""

    # def __init__(self, input_search, file_path=None):
    #     """Initialise an nlp_search object.
        
    #     Parameters
    #     ----------
    #     input_search (str) : input text to be searched.
    #     file_path (str) : Path of the file in which the text is to be searched.
        
    #     """
