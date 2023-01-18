from markovian.collections.lp_hashtable import LPHashtable
import math

HASH_CELLS = 57
TOO_FULL = 0.5
GROWTH_RATIO = 2

class Markov:
    def __init__(self, k, text):
        """
        Construct a new k-order markov model using the text 'text'.
        """
        self.k = k
        self.text = text
        self.hashtable = LPHashtable(HASH_CELLS, 0)

    def log_probability(self, s):
        """
        Get the log probability of string "s", given the statistics of
        character sequences modeled by this particular Markov model
        This probability is *not* normalized by the length of the string.
        """
        k_table = self.markov_model(self.text)
        S = self.len_unique_s
        log_prob = 0

        for i in range(len(s)):
            k_string, k_1_string = self.find_string(s, i)
            N = k_table[k_string]
            M = k_table[k_1_string]
            log_prob += math.log((M + 1)/(N + S))

        return log_prob

    def markov_model(self, text):
        unique_s = set()
        for i in range(len(text)):
            unique_s.add(text[i])
            string, string_plus_1 = self.find_string(text, i)
            self.hashtable[string] += 1
            self.hashtable[string_plus_1] += 1

        self.len_unique_s = len(unique_s)

        return self.hashtable

    def find_string(self, text, i):
        text = text * self.k
        string = text[i:i + self.k]
        string_plus_1 = text[i:i + self.k + 1]
        
        return string, string_plus_1
