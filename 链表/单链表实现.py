class Node():
    def __init__(self, value=None, next=None):
        self._value = value
        self._next = next

    def getValue(self):
        return self._value

    def setValue(self, new_value):
        self._value = new_value

    def getNext(self):
        return self._next

    def setNext(self, new_next):
        self._next = new_next


class LinkedList():
    # 初始化链表为空表
    def __init__(self):
        self._head = Node()

    def is_empty(self):
        return self._head == Node

    def add(self, value):
        newnode = Node(value)
        newnode.setNext(self._head)
        self._head = newnode

    def size(self):
        current = self._head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def append(self, value):
        newnode = Node(value)
        if self.is_empty():
            self._head = newnode
        else:
            current = self._head
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(newnode)

    def search(self, value):
        current = self._head
        foundValue = False
        while current != None and not foundValue:
            if current.getValue() == value:
                foundValue = True
            else:
                current = current.getNext()
        return foundValue

    def index(self, value):
        current = self._head
        count = 0
        found = None
        while current != None and not found:
            if current.getValue() == value:
                found = True
            else:
                current = current.getNext()
                count += 1
        if found:
            return count
        else:
            raise ValueError('%s is not in LinkedList' % value)

    def remove(self, value):
        current = self._head
        pre = None
        while current != None:
            if current.getValue() == value:
                if not pre:
                    self._head = current.getNext()
                else:
                    pre.setNext(current.getNext())
                break
            else:
                pre = current
                current = current.getNext()

    def insert(self, pos, value):
        if pos <= 1:
            self.add(value)
        elif pos > self.size():
            self.append(value)
        else:
            tmp = Node(value)
            count = 0
            pre = None
            current = self._head
            while count < pos:
                count += 1
                pre = current
                current = current.getNext()
            pre.setNext(tmp)
            tmp.setNext(current)
