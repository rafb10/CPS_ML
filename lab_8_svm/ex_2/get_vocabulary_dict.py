#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv

from typing import Dict


def get_vocabulary_dict() -> Dict[int, str]:
    """Read the fixed vocabulary list from the datafile and return.

    :return: a dictionary of words mapped to their indexes
    """

    # FIXME: Parse data from the 'data/vocab.txt' file.
    # - The file is saved in tab-separated values (TSV) format.
    # - Each line contains a word's ID and the word itself.
    # The output dictionary should map word's ID on the word itself, e.g.:
    #   {1: 'aa', 2: 'ab', ...}
    
    voc_dict = {}
    
    file1 = open('data/vocab.txt', 'r') 
    Lines = file1.readlines() 
  
    count = 0
    # Strips the newline character 
    for line in Lines: 
        num, word = line.split() #('\t')
        voc_dict[int(num)] = word

    return voc_dict
