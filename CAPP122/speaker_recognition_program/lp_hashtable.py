# TODO(1): import Hashtable here
from .hashtable import Hashtable

class LPHashtable(Hashtable):
    # polynomial constant, used for _hash
    P_CONSTANT = 37
    # if the total number of items / capacity exceeds this value, rehash
    TOO_FULL = 0.5
    # factor by which capacity should grow during a rehash
    GROWTH_RATIO = 2

    def __init__(self, capacity, default_value):
        # TODO(2): implement this constructor
        # use a single list named `_items` to store the items in your hashtable
        self.capacity = capacity
        self.default_value = default_value
        self._items = [(None, self.default_value)] * self.capacity
        self.items_added = 0

    def _hash(self, key):
        hash_value = 0
        for i in key:
            hash_value = hash_value * self.P_CONSTANT + ord(i)
        return hash_value % self.capacity

    def __setitem__(self, key, val):
        index = self._hash(key)
        for i in range(self.capacity):
            if self._items[index][0] is None:
                self._items[index] = (key, val)
                self.items_added += 1
                break
            if self._items[index][0] is key:
                self._items[index] = (key, val)
                break
            index = (index + 1) % self.capacity

        if self.items_added / self.capacity > self.TOO_FULL:
            self.capacity = self.capacity * self.GROWTH_RATIO
            self.rehash()

    def rehash(self):
        new_items = [(None, self.default_value) for _ in range(self.capacity)]
        old_list = [oldkv for oldkv in self._items if oldkv != (None, self.default_value)]
        self._items = new_items
        self.items_added = 0

        for key, value in old_list:
            if key != None:
                self.__setitem__(key, value)

    def __getitem__(self, key):
    #look for thing that is  set, if there are no collisions key will be
    #if something there, look through each element until it is empty
    #(incrementally +1)
        index = self._hash(key)
        for _ in range(self.capacity):
            if self._items[index][0] is None:
                return self.default_value
            if self._items[index][0] is key:
                return self._items[index][1]
            index = (index + 1) % self.capacity
        return self.default_value

    def __len__(self):
        return self.items_added

    def display(self):
        for idx, stored in enumerate(self._items):
            if stored:
                print("{} {} {}".format(idx, stored[0], stored[1]))
            else:
                print(f"{idx:<2} EMPTY")
