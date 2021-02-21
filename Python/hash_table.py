class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for _ in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for  char in key:
            h += ord(char)
        return h % self.MAX

    def __delitem__(self, key):
        h = self.get_hash(key)
        for i, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[h].pop(i)
                


    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        
        for i, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[h][i] = (key, value)
                return
        
        self.arr[h].append((key, value))

ht = HashTable()
ht['monday 6'] = 230
ht['monda'] = 12
ht['monday 109'] = 451
ht['monday 190'] = 66
print(ht['monday 109'])
del ht['monday 109']
print(ht.arr)