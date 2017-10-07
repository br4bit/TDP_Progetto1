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
        _node = Node(x, None, None)
        if self._head is not None:  # se la testa non è None allora il precedente del nuovo nodo diventa la coda e il successivo None
            _node._prev = self._tail  # il prcedente del nuovo nodo linka alla coda
            _node._next = None  # il successivo del nuovo nodo linka a None
            self._tail._next = _node  # il successivo della coda linka al nuovo nodo
            self._tail = _node  # il nuovo nodo è anche la nuova coda
        else:  # se la testa è None allora non c'è ancora nessun nodo, quindi il nuovo nodo è anche la coda
            self._head = self._tail = _node


    def __str__(self):
        result = ""
        curr_node = self._head
        while curr_node is not None:
            result+='['+str(curr_node._value)+'],'
            curr_node=curr_node._next
        return result
