class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        # Left = least recent, right = most recent
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        

    def get(self, key: int) -> int: #O(1)
        if key in self.cache:
            #update most recent
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None: #O(1)
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            #remove from the list and delete the least recent from cache
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
    #remove node from list
    def remove(self,node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    #insert at right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)