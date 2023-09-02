""" least recently used cache. 
    inserts into cache. if cache is full, least recently used element
    is removed to make space."""

class LRUcache:
    def __init__(self,size):
        self.cache = {}
        self.size = size
    
    def get(self,data):
        if data not in self.cache:
            return -1
        else:
            out = self.cache[data]
            del self.cache[data]
            self.cache[data] = out
            return out

    def put(self,key,data):
        if key in self.cache:
            del self.cache[key]
        self.cache[key] = data
        if len(self.cache) > self.size:
            least = list(self.cache.keys())[0]
            del self.cache[least]

cache = LRUcache(2)
  
cache.put(1, 1)
print(cache.cache)
cache.put(2, 2)
print(cache.cache)
cache.get(1)
print(cache.cache)
cache.put(3, 3)
print(cache.cache)
cache.get(2)
print(cache.cache)
cache.put(4, 4)
print(cache.cache)
cache.get(1)
print(cache.cache)
cache.get(3)
print(cache.cache)
cache.get(4)
print(cache.cache)