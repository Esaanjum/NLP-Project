# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 10:02:18 2023

@author: Esa
"""
import spacy
import PyPDF2

import os

# spacy english model (large)
nlp = spacy.load('en_core_web_lg')

# method for reading a pdf file
def readPdfFile(filename, folder_name) -> list:
    '''read pdf file and return its text'''
    
    # storing path of PDF-Documents folder
    data_path = str(os.getcwd()) + "\\" + folder_name

    file = open(data_path + "\\" + filename, mode="rb")

    # looping through pdf pages and storing data
    pdf_reader = PyPDF2.PdfReader(file)
    num_pages = len(pdf_reader.pages)

    # traverse through each page and store data as an element in list
    text = []
    for page_num in range(0, num_pages):
        current_page = pdf_reader.pages[page_num]
        text.append(current_page.extract_text().replace("\n","").lower())
        
    return text

