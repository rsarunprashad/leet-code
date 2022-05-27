    # Hash function to store large number of items in short space
# extract hash code of key to identify index at which the item will be stored
# More than one item can be 

class MyHashSet:

    def __init__(self):
        
        self.bucket_size = 100;
        self.buckets = [None] * self.bucket_size
        
    def compute_hash(self, key):
        
        return key % self.bucket_size
        

    def add(self, key: int) -> None:
        index = self.compute_hash(key)
        if self.buckets[index] is None:
            self.buckets[index]=[]
        self.buckets[index].append(key)


    def remove(self, key: int) -> None:
        index = self.compute_hash(key)
        bucket = self.buckets[index]
        if bucket is not None :
            while key in bucket:
                bucket.remove(key)

    def contains(self, key: int) -> bool:
        index = self.compute_hash(key)
        bucket = self.buckets[index]
        if bucket is not None :
            for item in bucket:
                if item == key:
                    return True
        return False


    
o=MyHashSet()
o.add(2)
o.add(2)
o.remove(2)
print(o.contains(2))
print(o.buckets)