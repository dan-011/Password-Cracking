class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link


def print_nodes(node):
    if node is None:
        # Base case
        print()
    else:
        # Print the current node
        print('->', node.data, end=' ')
        # Make a recursive call
        print_nodes(node.link)


class LinkedList:
    def __init__(self):
        self._head = None
        # No counter attribute -> __len__ will be implemented recursively

    def add_first(self, item):
        self._head = Node(item, self._head)

    def remove_first(self):
        if self._head is not None:
            item = self._head.data
            self._head = self._head.link
            return item
        else:
            raise RuntimeError('Cannot remove from an empty list.')

    def add_last(self, item):
        self._add_last(self._head, item)

    def _add_last(self, node, item):
        if node is None:
            self.add_first(item)
        elif node.link is None:
            node.link = Node(item)
        else:
            self._add_last(node.link, item)
    
    # For demonstration and debug purposes: Prints all the elements
    def print_all(self):
        # Calls a recursive helper function
        print_nodes(self._head)

    # Returns the length of the linked list
    def _len(self, node):
        if node is None:
            return 0
        else:
            return 1 + self._len(node.link)

    def __len__(self):
        # Implement recursively, using a helper function
        return self._len(self._head)


    # Sum all the elements in the linked list
    def sum_all(self):
        # Implement recursively, using a helper function
        return self._sum_all(self._head, 0)

    def _sum_all(self, node, _sum):
        if node is None:
            return _sum
        else:
            _sum += node.data
            return self._sum_all(node.link, _sum)

    # Create a deep copy: Create a new linked list with all its data copied
    def deep_copy(self):
        # Implement recursively, using a helper function        
        copy = LinkedList()
        copy._head = self._deep_copy(self._head)
        return copy

    def _deep_copy(self, node):
        if node is None:
            return None
        else:
            copy_node = Node(node.data)
            copy_node.link = self._deep_copy(node.link)
            return copy_node

    # Reverses the list in linear time, no copying of the data
    def reverse(self):
        # Implement recursively, using a helper function
        self._head = self._reverse(self._head)
    def _reverse(self, node):
        if node.link is None:
            return node
        else:
            tail = self._reverse(node.link)
            node.link.link = node
            node.link = None
            return tail


if __name__ == '__main__':
    ll = LinkedList()
    for i in range(10):
        ll.add_first(i)
    
    #len test
    assert len(ll) == 10
    
    # sum_all test
    assert ll.sum_all() == 45
    
    # deep_copy test
    ll1 = LinkedList()
    for i in range(10):
        ll1.add_last(i)
    
    ll2 = ll1.deep_copy()
    for i in range(10):
        assert ll1.remove_first() == ll2.remove_first()
    
    # reverse test
    ll3 = LinkedList()
    for i in range(3):
        ll3.add_first(i)
    ll3.print_all()
    ll3.reverse()
    ll3.print_all()
    for i in range(len(ll3)):
        assert ll3.remove_first() == i