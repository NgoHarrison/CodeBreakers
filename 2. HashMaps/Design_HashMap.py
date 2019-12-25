def hash(key: int) ->int:
    return key%1009

class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.store = [None] * 1009

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        index = hash(key)
        if self.store[index] is not None:
            cur = self.store[index]
            while cur is not None:
                if cur.key == key:
                    cur.key=key
                    cur.value=value
                    return
                elif cur.next == None:
                    temp = Node(key,value)
                    cur.next = temp
                else:
                    cur = cur.next
        else:
            self.store[index] = Node(key,value)
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        
        index = hash(key)
        cur = self.store[index]
        while cur is not None:
            if cur.key == key:
                return cur.value
            else:
                cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = hash(key)
            
            
        if self.store[index] is None:
            return -1
        else:
            cur = self.store[index]
            prev = self.store[index]
            if cur.key == key:
                self.store[index] = cur.next
            else:
                cur = cur.next
                while cur is not None:
                    if cur.key == key:
                        prev.next = cur.next
                        break
                    else:
                        cur = cur.next
                        prev = prev.next
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
