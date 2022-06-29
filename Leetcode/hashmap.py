class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.res = [-1] * 10000000

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        self.res[key] = value

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        return self.res[key]

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        self.res[key] = -1

# Your MyHashMap object will be instantiated and called as such:
hashMap = MyHashMap()
#obj.get("")
hashMap.put(1, 1)
hashMap.put(2, 2)
print(hashMap.res[0:10])
print(hashMap.get(1)) #            // returns 1
print(hashMap.get(3))    #        // returns -1 (not found)
hashMap.put(2, 1) #         // update the existing value
print(hashMap.res[0:10])
print(hashMap.get(2))     #       // returns 1
print(hashMap.res[0:10])
hashMap.remove(2) #          // remove the mapping for 2
hashMap.get(2)
print(hashMap.res[0:10])
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

