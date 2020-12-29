#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List

import numpy as np


def email_features(word_indices: List[int]) -> np.ndarray:
    """Convert a list of word IDs into a feature vector.

    :param word_indices: a list of word IDs
    :return: a feature vector from the word indices (a row vector)
    """

    # Total number of words in the dictionary
    n_words = 1899
    
    cnt = 1
    ret_vector = np.zeros(n_words)

    for i in word_indices:
        ret_vector[i] = 1.0
        
    return ret_vector
 
