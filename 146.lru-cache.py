#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#


# @lc code=start
class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            if node != self.head:
                self.move_to_top(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key is None or value is None:
            return
        if key in self.cache:
            node = self.cache[key]
            if node != self.head:
                self.move_to_top(node)
            self.cache.pop(key)
            self.head.val = value
            self.cache[key] = self.head
            return
        else:
            new = Node(key, value)
            if self.head:
                head = self.head
                head.prev = new
                new.next = head
            else:
                self.tail = new
            self.head = new
            self.cache[key] = new

        if len(self.cache) > self.capacity:
            self.cache.pop(self.tail.key)
            self.tail = self.tail.prev
            self.tail.next = None

    def print_node(self, current):
        elements = []
        while current:
            temp = f"{current.key}-{current.val}"
            elements.append(temp)
            current = current.next
        linked_list_string = " -> ".join(elements)
        print(linked_list_string + " -> None")

    def move_to_top(self, node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        node.next = self.head
        node.prev = None
        self.head.prev = node
        self.head = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
