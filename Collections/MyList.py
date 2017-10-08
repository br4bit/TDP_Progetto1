import Collections.Node


class MyList:
    # _head = None
    # _tail = None

    def __init__(self, *args):
        self._head = self._tail = None
        if args is not ():
            for index in range(len(args)):
                if type(args[index]).__name__ == 'list' or 'tuple':
                    try:
                        for k in range(len(args[index])):
                            self.append(args[index][k])
                    except TypeError:
                        for element in args:
                            self.append(element)

    def append(self, x):
        _node = Collections.Node.Node(x, None, None)
        if self._head is not None:  # if the head is not None the previously of new node become the tail and the
            #  next one None
            _node._prev = self._tail  # previously of new node linked to tail
            _node._next = None  # the next of new new node linked to None
            self._tail._next = _node  # the tail's next linked to new node
            self._tail = _node  # new node become the tail
        else:  # if the head is None there aren't node, so the new node is tail and the head
            self._head = self._tail = _node

    def clear(self):
        self.__init__()

    def reverse(self):
        temp = None
        curr_node = self._head
        # Swap next and prev for all nodes of
        # doubly linked list
        while curr_node is not None:
            temp = curr_node._prev
            curr_node._prev = curr_node._next # the previously is the next of the current node
            curr_node._next = temp # the next will be the previously of current before swap
            curr_node = curr_node._prev # update current node to previously
        # Before changing head, check for the cases like
        # empty list and list with only one node
        if temp is not None:
            self._head = temp._prev

    def pop(self, i=None):
        result = " "
        if i is None:
            ris = self._tail
            self._tail = ris._prev
            self._tail._next = None
            return ris._value
        else:
            curr_node = self._head
            k = 0
            try:
                while True:
                    if i > self.__len__():
                        break;
                    elif i == 0:
                        self._head = curr_node._next
                        result = curr_node
                        break;
                    elif i == self.__len__ () - 1:
                        result = self._tail
                        self._tail = result._prev
                        self._tail._next = None
                        break;
                    elif k == i and k < self.__len__():
                        result = curr_node
                        curr_node._prev._next = curr_node._next
                        curr_node._next._prev = curr_node._prev
                        break;
                    k += 1
                    curr_node = curr_node._next
            except AttributeError:
                return 'out of range'
            return result._value

    def __len__(self):
        i = 1
        node_iter = self._head
        while node_iter._next is not None:
            i += 1
            node_iter = node_iter._next
        return i

    def __str__(self):
        result = ""
        curr_node = self._head
        while curr_node is not None:
            result += '{0},'.format(str(curr_node._value))
            curr_node = curr_node._next
        return '[' + result[:-1] + ']'
