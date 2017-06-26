#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 17:35:52 2017

@author: simondefrenet
"""

import random

WORDLIST_FILENAME = "French words - Sheet2Fr.csv"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline().strip() # get the first line in line
    word = line.split(',')
    global language1
    global language2
    language1=word[0]
    language2=word[1]
    dictionnary=[]
    line = inFile.readline().strip() # get the first line in line
    i=0
    while line:
        word = line.split(',')
        dictionnary+=[word]
        line = inFile.readline().strip() # get the next line in line
        i+=1
    # wordlist: list of strings
    return dictionnary

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
        
dictionnary = loadWords()


'''
    elif test=="chooseenglish":
        choose("english")
    elif test=="choosecantonese":
        choose("cantonese")
'''
        