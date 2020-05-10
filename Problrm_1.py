class Node:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.next = None
        self.prev = None

class LRU_cache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.next = self.tail
        node.prev = p


    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p



    def get(self, key):
        if key in self.dic:
            n = self.dic[key]
            self._remove(n)
            self._add(n)
            return n.value
        return -1

    def set(self, key, value):
        n = Node(key, value)
        self._add(n)
        self.dic[key] = n
        if len(self.dic) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.dic[n.key]

our_cache = LRU_cache(5)
our_cache.set(1, 1);
our_cache.set(12, 12);
our_cache.set(3, 3);
our_cache.set(4, 4);
our_cache.set(22,22);
our_cache.set(2,2);
our_cache.set(1,1);
print(our_cache.get(1))
# expected answer is 1
print(our_cache.get(12))
# expected answer is -1 as 12 is not in  cache memory
print(our_cache.get(22))
# expected answer is 22


our_cache2 = LRU_cache(0)
our_cache2.set(5, 5)
our_cache2.set(6, 6)
print(our_cache2.get(6))
# expected answer is -1 as the size of cache is 0 so there is no element in the cache memory


our_cache3=LRU_cache(1)
our_cache3.set(4, 4);
#expected answer is 4
print(our_cache3.get(4))
our_cache3.set(6,6);
print(our_cache3.get(4))
# expected answer is -1 as 4 is not in  cache memory
