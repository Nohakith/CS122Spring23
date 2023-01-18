"""
CAPP 121: Analyzing Election Tweets

Jonathan Juarez

Analyze module

Functions to analyze tweets. 
"""

from gettext import find
import unicodedata
import sys

from basic_algorithms import find_top_k, find_min_count, \
augmented_term_frequency, inverted_term_frequency, tf_idf_score, find_salient

##################### DO NOT MODIFY THIS CODE #####################

def keep_chr(ch):
    '''
    Find all characters that are classifed as punctuation in Unicode
    (except #, @, &) and combine them into a single string.
    '''
    return unicodedata.category(ch).startswith('P') and \
        (ch not in ("#", "@", "&"))

PUNCTUATION = " ".join([chr(i) for i in range(sys.maxunicode)
                        if keep_chr(chr(i))])

# When processing tweets, ignore these words
STOP_WORDS = ["a", "an", "the", "this", "that", "of", "for", "or",
              "and", "on", "to", "be", "if", "we", "you", "in", "is",
              "at", "it", "rt", "mt", "with"]

# When processing tweets, words w/ a prefix that appears in this list
# should be ignored.
STOP_PREFIXES = ("@", "#", "http", "&amp")


#####################  MODIFY THIS CODE #####################


############## Part 2 ##############

def find_top_k_entities(tweets, entity_desc, k):
    '''
    Find the k most frequently occuring entitites.

    Inputs:
        tweets: a list of tweets
        entity_desc: a triple such as ("hashtags", "text", True),
          ("user_mentions", "screen_name", False), etc.
        k: integer

    Returns: list of entities
    '''
    key, subkey, case_sensitive = entity_desc

    list_of_entities = []
    for tweet in tweets:
        key_list = tweet['entities'][key]
        for kl in key_list:
            sb = kl[subkey]
            if case_sensitive == False:
                sb = sb.lower()
            list_of_entities.append(sb)

    top_k_entities = find_top_k(list_of_entities, k)
    
    return top_k_entities


# Task 2.2
def find_min_count_entities(tweets, entity_desc, min_count):
    '''
    Find the entitites that occur at least min_count times.

    Inputs:
        tweets: a list of tweets
        entity_desc: a triple such as ("hashtags", "text", True),
          ("user_mentions", "screen_name", False), etc.
        min_count: integer

    Returns: set of entities
    '''
    key, subkey, case_sensitive = entity_desc

    list_of_entities = []
    for tweet in tweets:
        key_list = tweet['entities'][key]
        for kl in key_list:
            sb = kl[subkey]
            if case_sensitive == False:
                sb = sb.lower()
            list_of_entities.append(sb)

    minimum_k_entities = find_min_count(list_of_entities, min_count)
    
    return minimum_k_entities



############## Part 3 ##############

# Pre-processing step and representing n-grams
def abridged_text_to_list(abridged_text, case_sensitive, stop_words):
    """
    Convert a list of abridged text string into a list of strings for each word
    Inputs:
        abridged_text: a string
        case_sensitive: (boolean) if False, converts words into lower case
        stop_words: (boolean) if True, stops common words from appearing on 
        final list
    Output:
        final_list (list): list with clean words
    """
    abridged_text_to_list = []
    for word in abridged_text.split():
        if word[0] in PUNCTUATION:
            word = word.lstrip(PUNCTUATION)  
        elif word[-1] in PUNCTUATION:
            word = word.rstrip(PUNCTUATION)
        abridged_text_to_list.append(word)

    clean_list = []
    for word in abridged_text_to_list:
        if word.startswith(STOP_PREFIXES):
            continue
        elif word == '':
            continue
        else:
            clean_list.append(word)
    
    final_list = []

    for word in clean_list:
        if case_sensitive == False:
            word = word.lower()
            final_list.append(word)
        else:
            final_list.append(word)

    no_stop_words_list = []
    for word in final_list:
        if stop_words == True:
            if word in STOP_WORDS:
                continue
            else:
                no_stop_words_list.append(word)
                
    if stop_words == True:
        return no_stop_words_list
    else:
        return final_list

def n_grams(n, abridged_text, case_sensitive, stop_words):
    """
    Compute n-grams of a tweet from clean list from abridged_test_to_list
    Inputs:
        n (integer): number of n-grams that will be generated as a tuple
    """
    clean_lst = abridged_text_to_list(abridged_text, case_sensitive, stop_words)
    n_gram_list = []
    for i in range(len(clean_lst)- n+1):
        n_gram_list.append(tuple(clean_lst[i:i+n]))
    
    return n_gram_list
        
# Task 3.1
def find_top_k_ngrams(tweets, n, case_sensitive, k):
    '''
    Find k most frequently occurring n-grams.

    Inputs:
        tweets: a list of tweets
        n: integer
        case_sensitive: boolean
        k: integer

    Returns: list of n-grams
    '''
    stop_words = True
      
    tokens = []
    for tweet in tweets:
        abridged_text = tweet['abridged_text']
        n_gram_list = n_grams(n, abridged_text, case_sensitive, stop_words)
        for gram in n_gram_list:
            tokens.append(gram)
    
    top_k_ngrams = find_top_k(tokens, k)

    return top_k_ngrams


# Task 3.2
def find_min_count_ngrams(tweets, n, case_sensitive, min_count):
    '''
    Find n-grams that occur at least min_count times.

    Inputs:
        tweets: a list of tweets
        n: integer
        case_sensitive: boolean
        min_count: integer

    Returns: set of n-grams
    '''

    stop_words = True
      
    tokens = []
    for tweet in tweets:
        abridged_text = tweet['abridged_text']
        n_gram_list = n_grams(n, abridged_text, case_sensitive, stop_words)
        for gram in n_gram_list:
            tokens.append(gram)
    
    min_ngrams = find_min_count(tokens, min_count)

    return min_ngrams


# Task 3.3
def find_salient_ngrams(tweets, n, case_sensitive, threshold):
    '''
    Find the salient n-grams for each tweet.

    Inputs:
        tweets: a list of tweets
        n: integer
        case_sensitive: boolean
        threshold: float

    Returns: list of sets of strings
    '''
    #use
    find_salient(docs, threshold)

    # REPLACE [] WITH A SUITABLE RETURN VALUE
    return []
