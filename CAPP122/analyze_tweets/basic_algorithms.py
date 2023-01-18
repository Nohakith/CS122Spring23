"""
CAPP 121: Analyzing Election Tweets

Jonathan Juarez

Basic algorithms module

Algorithms for efficiently counting and sorting distinct 'entities',
or unique values, are widely used in data analysis.
"""

import math
from util import sort_count_pairs

# Task 1.1
def count_tokens(tokens):
    '''
    Counts each distinct token (entity) in a list of tokens.

    Inputs:
        tokens: list of tokens (must be immutable)

    Returns: dictionary that maps tokens to counts
    '''
    token_dict = {}
    for t in tokens:
        if t not in token_dict:
            token_dict[t] = 0
        token_dict[t] += 1
    
    return token_dict


# Task 1.2
from itertools import count


def find_top_k(tokens, k):
    '''
    Find the k most frequently occuring tokens.

    Inputs:
        tokens: list of tokens (must be immutable)
        k: a non-negative integer

    Returns: list of the top k tokens ordered by count.
    '''

    #Error checking (DO NOT MODIFY)
    if k < 0:
        raise ValueError("In find_top_k, k must be a non-negative integer")

    #Turn count_token(tokens) dictionary into tuple list
    token_list = (count_tokens(tokens).items())
    #Use built in sor_count_pairs function to sort based on values first, 
    #keys second
    sorted_token_list = sort_count_pairs(token_list)

    tokens_only = []
    for token, count in sorted_token_list[:k]:
        tokens_only.append(token)
    
    return tokens_only


# Task 1.3
def find_min_count(tokens, min_count):
    '''
    Find the tokens that occur *at least* min_count times.

    Inputs:
        tokens: a list of tokens  (must be immutable)
        min_count: a non-negative integer

    Returns: set of tokens
    '''

    #Error checking (DO NOT MODIFY)
    if min_count < 0:
        raise ValueError("min_count must be a non-negative integer")

    token_set = set()
    token_list = (count_tokens(tokens).items())
    for token, counts in token_list:
        if counts >= min_count:
            token_set.add(token)

    return token_set

#For task 1.4
def augmented_term_frequency(tokens):
    """
    Calculate the augmented term frequency for each token in a list of tokens
    and return a dictionary with tokens mapped to augmented tf values
    
    """
    augmented_tf_dict = {}

    for token, counts in count_tokens(tokens).items():
        tf_value = counts/max(count_tokens(tokens).values())
        augmented_tf_value = (tf_value * 0.5) + 0.5
        augmented_tf_dict[token] = augmented_tf_value

    return augmented_tf_dict

#For 1.4
def inverted_term_frequency(docs):
    """
    Calculate the number of different documents that a token appears in
    """

    unique_token_set = set()

    for document in docs:
        for token in document:
            unique_token_set.add(token)

    idf_score_dict = {}

    for token in unique_token_set:
        total_tokens_indocs = 0
        for document in docs:
            if token in document:
                total_tokens_indocs += 1
        idf_score_dict[token] = total_tokens_indocs
                
    for token in idf_score_dict:
         idf_score_dict[token] = math.log(len(docs)/idf_score_dict[token])
    return idf_score_dict

#For 1.4
def tf_idf_score(docs):
    """
    Create list of a dictionary of calculated tf_idf_scores for each token
    for each document in docs
    """
    tf_idf_score = []
    idf_scores = inverted_term_frequency(docs)
    for i, document in enumerate(docs):
        tf_scores = augmented_term_frequency(document)
        tf_idf_score.append(tf_scores)
        for token, tfs in tf_idf_score[i].items():
            tf_idf_score[i][token] = tfs*idf_scores[token]

    return tf_idf_score

# Task 1.4
def find_salient(docs, threshold):
    '''
    Compute the salient words for each document.  A word is salient if
    its tf-idf score is strictly above a given threshold.

    Inputs:
      docs: list of list of tokens
      threshold: float

    Returns: list of sets of salient words
    '''
    
    salient_words_list = []
    for scores in tf_idf_score(docs):
        salient_words = set()
        for token, tf_idf in scores.items():
            if tf_idf > threshold:
                salient_words.add(token)
        salient_words_list.append(salient_words)
    
    return salient_words_list
