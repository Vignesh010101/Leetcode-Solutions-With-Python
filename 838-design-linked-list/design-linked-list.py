class MyLinkedList:
    class _Node:
        def __init__(self, val=None, prev=None, next=None):
            self._val = val
            self._prev = prev
            self._next = next

        def __str__(self):
            return f"{self._val}"

        def __repr__(self):
            return f"{self._val}"

    def __init__(self):
        self._head = self._Node(None)
        self._tail = self._Node(None)
        self._size = 0
        self._head._next = self._tail
        self._tail._prev = self._head

    def _getAtIndex(self, index) -> "_Node":
        curr = None
        if index == self._size-1:
            return self._tail._prev
        elif index == 0:
            return self._head._next
        if self._size - index < index:
            curr = self._tail._prev

            i = self._size - 1
            while i > index:

                curr = curr._prev
                i -= 1

        else:
            curr = self._head._next
            i = 0
            while i < index:
                curr = curr._next
                i += 1
        return curr

    def _insert_between(self, e, prev, succ) -> None:
        n = self._Node(e, prev, succ)
        prev._next = n
        succ._prev = n
        self._size += 1

    def get(self, index: int) -> int:
        if index >= self._size or self._size == 0:
            return -1
        curr = self._getAtIndex(index)
        return curr._val

    def addAtHead(self, val: int) -> None:
        self._insert_between(val, self._head, self._head._next)

    def addAtTail(self, val: int) -> None:
        self._insert_between(val, self._tail._prev, self._tail)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self._size:
            return
        if index == 0:
            self.addAtHead(val)
        elif index == self._size :
            self.addAtTail(val)
        else: 
            curr = self._getAtIndex(index)
            self._insert_between(val, curr._prev, curr)

    def deleteAtIndex(self, index: int) -> None:
        
        if 0<=index < self._size:
            curr = self._getAtIndex(index)
            curr._prev._next = curr._next
            curr._next._prev = curr._prev
            self._size -= 1
            curr = None