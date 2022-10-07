def find_duplicate(L):
    n = len(L)
    left = 0
    right = n-1
    while right - left > 1:
        expected_middle = (L[right]-L[left])//2 + L[left]
        median = (left + right)//2
        length = (right - left) + 1
        print("left = {}, right = {}".format(left, right))
        if length%2 == 0:
            if L[median] == expected_middle:
                left = median
            else:
                right = median
        else:
            if L[median] == expected_middle:
                right = median
            else:
                left = median
    return L[left]

assert find_duplicate([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]) == 26
assert find_duplicate([1,2,3,3,4]) == 3
assert find_duplicate([1,1]) == 1
# def find_duplicate(L):
#     n = len(L)
#     left = 0
#     right = n-1
#     while right - left > 0:
#         expected_middle = (L[right]-L[left])//2 + L[left]
#         median = (left + right)//2
#         length = (right - left) + 1
#         if length%2 == 0:
#             if L[median] == expected_middle:
#                 left = median + 1
#             else:
#                 right = median
#         else:
#             if L[median] == expected_middle:
#                 right = median
#             else:
#                 left = median + 1
#     return L[left]


def quickselect(L, left = 0, right = None):
    if right is None: right = len(L)
    pivot = right - 1
    i,j = left, pivot - 1

    while i < j:
        while L[i] < L[pivot]: i += 1
        while i < j and L[j] >= L[pivot]: j -= 1
        if i < j:
            L[i], L[j] = L[j], L[i]
    if L[pivot] < L[i]:
        L[pivot], L[i] = L[i], L[pivot]
        pivot = i

    median = len(L) -1 //2
    if pivot == median: return L[pivot]
    elif pivot > median: return quickselect(L, left, pivot)
    else: return quickselect(L, pivot + 1, right)

class BSTNode:
    def __init__(self, key, item):
        self.key = key
        self.item = item
        self.weight = 0
        self.left = None
        self.right = None

    def put(self, key, item):
        if self.key == key:
            self.item = item
        elif key < self.key:
            if self.left is not None:
                self.left.put(key, value)
            else:
                self.left = BSTNode(key, item)
        elif key > self.key:
            if self.right is not None:
                self.right.put(key,item)
            else:
                self.right = BSTNode(key, item)
        self.update_weight()
        return self
    def update_weight(self):
        if self.left is not None:
            left_weight = self.left.weight
        else: left_weight = 0
        if self.right is not None:
            right_weight = self.right.weight
        else: right_weight = 0
        self.weight = left_weight + right_weight + 1

    def get(self, key):
        if self.key == key:
            return self.item
        elif key < self.key:
            if self.left is not None:
                return self.left.get(key)
        elif key > self.key:
            if self.right is not None:
                return self.right.get(key)
        raise KeyError()
    def floor(self, key):
        if self.key == key: return self.item
        elif key < self.key: return self.left.floor(key)
        elif key > self.key:
            if self.right is None or self.right.key > key:
                return self.item
            else:
                return self.right.floor(key)
    def __str__(self):
        return str((self.key, self.item))
    def pre_order(self):
        yield self
        if self.left is not None:
            yield from self.left.pre_order()
        if self.right is not None:
            yield from self.right.pre_order()
    def post_order(self):
        if self.left is not None:
            yield from self.left.post_order()
        if self.right is not None:
            yield from self.right.post_order()
        yield self
    def in_order(self):
        if self.left is not None:
            yield from self.left.in_order()
        yield self
        if self.right is not None:
            yield from self.right.in_order()
class BST:
    def __init__(self):
        self.root = None
    
    def put(self, key, item):
        if self.root is None:
            self.root = BSTNode(key, item)
        else:
            self.root.put(key, item)

    def get(self, key):
        if self.root is not None:
            self.root.get(key)
        else: raise KeyError
    
    def floor(self, key):
        if self.root is not None:
            self.root.floor(key)
        else:
            raise KeyError()
    def in_order(self):
        yield from self.root.in_order()
    def pre_order(self):
        yield from self.root.pre_order()
    def post_order(self):
        yield from self.root.post_order()
tree = BST()
for i in range(10):
    tree.put(i,str(i))
class Stack:
    def __init__(self):
        self.L = []
    def push(self, item):
        self.L.append(item)
    def pop(self):
        return self.L.pop()
    def __iter__(self):
        return StackIterator(self)
class StackIterator:
    def __init__(self, stack):
        self.stack = stack
        self.counter = len(stack.L) -1
    def __next__(self):
        while self.counter >= 0:
            item = self.stack.L[self.counter]
            self.counter -= 1
            return item
        raise StopIteration()
