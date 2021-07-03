class Hashtable:

    def __init__(self, m, hash_func=hash):
        """ initial hash table, m empty entries, uses hash_func """
        self.table = [[] for i in range(m)]
        self.hash_mod = lambda key: hash_func(key) % m

    def find(self, item):
        """ returns True if item in hashtable, False otherwise  """
        i = self.hash_mod(item)
        chain = self.table[i]
        return item in chain  # a hidden loop

    def insert(self, item):
        """ insert an item into table, if not there """
        i = self.hash_mod(item)
        chain = self.table[i]
        if item not in chain:  # a hidden loop
            chain.append(item)

