class Node:
    def __init__(self, key, value, next=None, prev=None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keys_to_nodes = {}
        self.left = Node(-1,-1)
        self.right = Node(-1,-1)
        self.left.next = self.right
        self.right.prev = self.left 

    def get(self, key: int) -> int:
        if key not in self.keys_to_nodes:
            return -1
        
        node = self.keys_to_nodes[key]
        self.remove(node)
        self.insert_as_mru(node)
        return node.value

    # l 55 88 66 99 r
    def put(self, key: int, value: int) -> None:
        new_node = Node(key, value)
        
        # if key exists, remove the old node from ll
        if key in self.keys_to_nodes:
            old_node = self.keys_to_nodes[key]
            self.remove(old_node)
        
        self.keys_to_nodes[key] = new_node
        self.insert_as_mru(new_node)

        if len(self.keys_to_nodes) > self.capacity:
            # remove first left node
            lru_node = self.left.next
            del self.keys_to_nodes[lru_node.key] 
            self.remove(self.left.next)

    # l 99 r
    def remove(self, node):
        print(f"Node to remove: {node.value}")
        print(f"Before: {self.iterate_ll()}")
        l = node.prev
        r = node.next
        l.next = r
        r.prev = l
        node.prev = None
        node.next = None
        print(f"After: {self.iterate_ll()}")
    
    # l 99 r    new_node: 99
    def insert_as_mru(self, node):
        print(f"Node to insert as MRU: {node.value}")
        print(f"Before: {self.iterate_ll()}")
        old_mru = self.right.prev
        old_mru.next = node
        node.prev = old_mru
        node.next = self.right
        self.right.prev = node
        print(f"After: {self.iterate_ll()}")

    def iterate_ll(self):
        curr_node = self.left
        ll = []
        while curr_node:
            ll.append(str(curr_node.value))
            curr_node = curr_node.next
        return f"LinkedList: {"->".join(ll)}"
        
















