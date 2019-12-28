def helper(dl):
    cur = dl.head.next
    while cur.next:
        print(cur.key,cur.value)
        cur = cur.next
    print('-----------')

class DoubleNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
        
class LRUCache:
    def __init__(self,capacity):
        self.head = DoubleNode('head','head')
        self.tail = DoubleNode('tail','tail')
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.cache = {}
        
    def get(self,key):
        if key in self.cache:
            temp = self.cache[key]
            self.delete(temp)
            self.add(temp)
            return temp.value
        else:
            return -1
    def put(self,key,value):
        if key in self.cache:
            self.delete(self.cache[key])
        node = DoubleNode(key,value)
        self.add(node)
        self.cache[key]=node
        if len(self.cache) > self.capacity:
            temp = self.tail.prev
            self.delete(temp)
            del self.cache[temp.key]
            
    def delete(self,node):
        previous = node.prev
        after = node.next
        previous.next = after
        after.prev = previous
        
    def add(self,node):
        temp = self.head.next
        self.head.next = node
        node.prev = self.head
        temp.prev = node
        node.next = temp
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
