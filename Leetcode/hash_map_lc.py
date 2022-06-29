class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.capacity = 100
        self.internal_map = [[] for _ in range(self.capacity)]
        #print(self.internal_map)

    def hash_function(self, key):
        return key % self.capacity

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hash_key = self.hash_function(key)
        bucket = self.internal_map[hash_key]

        found = False
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket[i][1] = value
                found = True
                print("FOUND")
                break

        if not found:
            bucket.append([key, value])
        print(bucket)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hash_key = self.hash_function(key)
        bucket = self.internal_map[hash_key]

        for i in range(len(bucket)):
            if bucket[i][0] == key:
                return bucket[i][1]
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hash_key = self.hash_function(key)
        bucket = self.internal_map[hash_key]

        for i in range(len(bucket)):
            if bucket[i][0] == key:
                temp = bucket[i]
                bucket[i] = bucket[0]
                bucket[0] = temp
                bucket.pop(0)
                break


hashMap = MyHashMap()
#obj.get("")
hashMap.put(1, 1)
hashMap.put(2, 2)
hashMap.put(2, 2)
""""
hashMap.put(2, 2)
#print(hashMap.res[0:10])
print(hashMap.get(1)) #            // returns 1
print(hashMap.get(3))    #        // returns -1 (not found)
hashMap.put(2, 1) #         // update the existing value
#print(hashMap.res[0:10])
print(hashMap.get(2))     #       // returns 1
#print(hashMap.res[0:10])
hashMap.remove(2) #          // remove the mapping for 2
hashMap.get(2)
#print(hashMap.res[0:10])
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
"""

