from collections.abc import MutableMapping
from abc import abstractmethod


class Hashtable(MutableMapping):

    @abstractmethod
    def _hash(self, key):
        """
        This method takes in a string and returns an integer value
        between 0 and self.capacity.

        This particular hash function uses Horner's rule to compute a large polynomial.

        See https://www.cs.umd.edu/class/fall2019/cmsc420-0201/Lects/lect10-hash-basics.pdf
        """
        pass

    @abstractmethod
    def __setitem__(self, key, val):
        pass

    @abstractmethod
    def __getitem__(self, key):
        pass

    @abstractmethod
    def __len__(self):
        pass

    def __delitem__(self, key):
        """
        You do not need to implement __delitem__ for this assignment.
        This stub is needed to satisfy `MutableMapping` however.)
        """
        raise NotImplementedError()

    def __iter__(self):
        """
        You do not need to implement __iter__ for this assignment.
        This stub is needed to satisfy `MutableMapping` however.)

        Note, by not implementing __iter__ your implementation of Markov will
        not be able to use things that depend upon it,
        that shouldn't be a problem but you'll want to keep that in mind.
        """
        raise NotImplementedError()
