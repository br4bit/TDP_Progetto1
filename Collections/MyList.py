from Collections.Node import Node


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
        """Add an item to the end of the list."""
        _node = Node(x, None, None)
        if self._head is not None:  # if the head is not None the previously of new node become the tail and the
            #  next one None
            _node._prev = self._tail  # previously of new node linked to tail
            _node._next = None  # the next of new new node linked to None
            self._tail._next = _node  # the tail's next linked to new node
            self._tail = _node  # new node become the tail
        else:  # if the head is None there aren't node, so the new node is tail and the head
            self._head = self._tail = _node

    def clear(self):
        """Remove all items from the list"""
        self.__init__()

    def isEmpty(self):
        if self.__bool__():
            return False
        else:
            return True

    def count(self, x):
        count = 0
        curr_node = self._head
        """Return the number of times x appears in the list."""
        for i in range(0, self.__len__()):
            if curr_node._value == x:
                count += 1
            curr_node = curr_node._next
        return count

    def extend(self, iterable):
        """Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable."""
        for value in iterable:
            self.append(value)

    def insert(self,i,x):
        new_node = Node(x,None,None)
        curr_node = self._head
        if i > self.__len__():
            return 'index out of range'
        #list is empty
        if self.isEmpty():
            self._head = new_node
            self._head._prev = self._head
        else:
            if i == 0:
                new_node._next = self._head
                self._head = new_node
                if self.__len__() == 0:
                    self._tail = new_node
                return
            elif i == self.__len__():
                self.append(new_node._value)
                return
            else:
                for k in range(0, i-1):
                  curr_node = curr_node._next
                  new_node._next = curr_node._next
                  new_node._prev = curr_node
                  if curr_node._next is not None:
                     curr_node._next._prev = new_node
                curr_node._next = new_node


    def remove(self, x):
        """Remove the first item from the list whose value is x. It is an error if there is no such item."""
        curr_node = self._head
        k = 0
        while curr_node is not None:
            if curr_node._value == x:
                return self.pop(k)
            k += 1
            curr_node = curr_node._next
        else:
            return 'No such ' + str(x)

    def reverse(self):
        """Reverse the elements of the list in place."""
        temp = None
        curr_node = self._head
        self._tail = curr_node
        # Swap next and prev for all nodes of
        # doubly linked list
        while curr_node is not None:
            temp = curr_node._prev
            curr_node._prev = curr_node._next  # the previously is the next of the current node
            curr_node._next = temp  # the next will be the previously of current before swap
            curr_node = curr_node._prev  # update current node to previously
        # Before changing head, check for the cases like
        # empty list and list with only one node
        if temp is not None:
            self._head = temp._prev

    def pop(self, i=None):
        """Remove the item at the given position in the list, and return it. If no index is specified,
        a.pop() removes and returns the last item in the list. (The square brackets around the i in the method
        signature denote that the parameter is optional, not that you should type square brackets at that position. """
        result = None
        if i is None:
            ris = self._tail
            self._tail = ris._prev
            self._tail._next = None
            return ris._value
        else:
            curr_node = self._head
            k = 0
            try:
                if i == 0:
                    self._head = curr_node._next
                    self._head._prev = None
                    return curr_node._value
                elif i == self.__len__() - 1:
                    result = self._tail
                    self._tail = result._prev
                    self._tail._next = None
                    return result._value
                elif i >= self.__len__():
                    raise AttributeError
                while k < self.__len__():
                    if k == i:
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

    def __bool__(self):
        if self._head:
            return True
        else:
            return False

    def __getitem__(self, i):
        curr_node = self._head
        if i >= self.__len__():
            raise IndexError
        elif i == 0:
            return self._head
        for k in range(0,self.__len__()):
            if k == i:
                return curr_node
            curr_node = curr_node._next

    def __add__(self, other):
        """adds a an iterable data structure to the double linked list"""
        ret_my_list = MyList()
        for item in self:
            ret_my_list.append(item._value)
        for item in other:
            ret_my_list.append(item)
        return ret_my_list
