#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
from typing import List

from nltk import PorterStemmer

from get_vocabulary_dict import get_vocabulary_dict


def process_email(email_contents: str) -> List[int]:
    """Pre-process the body of an email and return a list of indices of the
    words contained in the email.

    :param email_contents: the body of an email
    :return: a list of indices of the words contained in the email
    """

    # Load the vocabulary.
    vocabulary_dict = get_vocabulary_dict()

    # Initialize the return value.
    word_indices = []

    # ========================== Preprocess Email ===========================

    # Find the Headers ( \n\n and remove )
    # Uncomment the following lines if you are working with raw emails with the
    # full headers

    # header_token = '\n\n'
    # header_start = email_contents.find(header_token)
    # email_contents = email_contents[header_start+len(header_token):]

    # FIXME: Convert email content to lower case.
    print('1\n')
    print(email_contents)    
    
    email_contents = str(email_contents).lower()
    

    # Strip all HTML
    # Looks for any expression that starts with < and ends with > and replace
    # and does not have any < or > in the tag it with a space
    email_contents = re.sub('<[^<>]+>', ' ', email_contents)

    # FIXME: Handle numbers.
    # Convert all sequences of digits (0-9) to a 'number' token.
    email_contents = re.sub(r'\d+\s', 'number', email_contents)

    # FIXME: Handle URLs.
    # Convert all strings starting with http:// or https:// to a 'httpaddr' token.
    email_contents = re.sub('http://\S*\s', 'httpaddr ', email_contents)
    email_contents = re.sub('https://\S*\s', 'httpaddr ', email_contents)

    # FIXME: Handle email addresses.
    # Convert all strings with @ in the middle to a 'emailaddr' token.
    email_contents = re.sub('\s\S*@\S*\s', ' emailaddr ', email_contents)

    # FIXME: Handle $ sign
    # Convert all sequences of $ signs to a 'dollar' token.
    email_contents = re.sub('\$', ' dollar ', email_contents)
    #email_contents = re.sub('\s\$*', ' dollar ', email_contents)

    # ========================== Tokenize Email ===========================

    # Output the email to screen as well
    print('\n==== Processed Email ====\n\n')

    # Process file
    col = 0

    # Tokenize and also get rid of any punctuation
    tokens = re.split('[ @$/#.-:&*\+=\[\]?!\(\)\{\},''">_<;#\n\r]', email_contents)
    
    print("hjhjhjh\n")
    print(tokens)

    for token in tokens:

        # Remove any non alphanumeric characters
        token = re.sub('[^a-zA-Z0-9]', '', token)

        # Stem the word 
        token = PorterStemmer().stem(token.strip())

        # Skip the word if it is too short
        if len(token) < 1:
            continue

        for number, word in vocabulary_dict.items():
            if token == word:
                word_indices.append(number)


        # Print to screen, ensuring that the output lines are not too long
        if (col + len(token) + 1) > 78:
            print('')
            col = 0
        print('{} '.format(token), end='', flush=True)
        col = col + len(tokens) + 1

    # Print footer
    print('\n\n=========================\n')

    return word_indices
