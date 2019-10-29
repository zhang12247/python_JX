class Node():
    def __init__(self):
        self._value = None
        self._next = None

    def setValue(self, newValue):
        self._value = newValue

    def setNext(self, newNext):
        self._next = newNext

    def getValue(self):
        return self._value

    def getNext(self):
        return self._next

    def __str__(self):
        return str(self._value)


class LinkedList():
    def __init__(self):
        self._head = None

    def add(self, value):
        new_Node = Node()
        new_Node.setValue(value)
        new_Node.setNext(self._head)
        self._head = new_Node

    def append(self, value):
        new_Node = Node()
        new_Node.setValue(value)
        current = self._head
        while current.getNext() != None:
            current = current.getNext()
        current.setNext(new_Node)

    def is_empty(self):
        return self._head == None

    def insert(self, pol, value):
        if pol <= 1:
            self.add(value)
        elif pol > self.size():
            self.append(value)
        else:
            pre = self.get(pol)
            current = pre.getNext()
            new_Node = Node()
            new_Node.setValue(value)
            new_Node.setNext(current)
            pre.setNext(new_Node)

    def search(self, value):
        pass

    def index(self, value, position=0):
        pass

    def remove(self, value):
        pass

    def size(self):
        count = 0
        current = self._head
        if self.is_empty():
            return count
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def get(self, pol):
        count = 1
        current = self._head
        while count < pol:
            current = current.getNext()
            count += 1
        return current

    def __str__(self):
        a = ""
        current = self._head
        while current != None:
            a = a + str(current.getValue()) + ','
            current = current.getNext()
        return a


if __name__ == '__main__':
    newlist = LinkedList()
    print(newlist.size())
    newlist.add('5')
    print(newlist.size())
    newlist.add(6)
    newlist.append(8)
    newlist.insert(3,'9')
    newlist.insert(3,3)
    newlist.insert(3,1)
    newlist.insert(100, 7)
    a = newlist.get(1)
    print(a)
    print(newlist)
