
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def getVal(self):
        return self.val

    def setVal(self, val):
        self.val = val

    def getNext(self):
        return self.next

    def setNext(self, node):
        if node is None or isinstance(node, Node):
            self.next = node
        else:
            raise Exception("Next node must be of type Node or None")

    def __repr__(self) -> str:
        return f"{self.getVal()!r}"

    def isLast(self):
        return self.next is None


def getKey(obj):
    """This function should be overwritten (if needed) to get the key for its corresponding object.
        Example: class Object:
                    name: str
                    key: int

                def getKey(obj: Object):
                        return obj.key

        Depending on the data the return value might be different
    """
    return obj


class LinkedList:
    def __init__(self):
        self.first = None

    def getFirst(self):
        return self.first

    def setFirst(self, node: Node):
        if node is None or isinstance(node, Node):
            self.first = node
        else:
            raise Exception("Next node must be of type Node or None")

    def isEmpty(self):
        return self.first is None

    def traverse(self, func=print):
        current = self.getFirst()
        while (current):
            func(current.getVal())
            current = current.getNext()

    def insert(self, newValue):
        newNode = Node(newValue, self.getFirst())
        self.setFirst(newNode)

    def find(self, goal, key=getKey):
        current = self.getFirst()
        while (current):
            if key(current.getVal()) == goal:
                return current

            current = current.getNext()

    def insertAfter(self, goal, newValue, key=getKey):
        nodeBefore = self.find(goal, key)
        if nodeBefore is None:
            return False

        newNode = Node(newValue, nodeBefore.getNext())
        nodeBefore.setNext(newNode)

    # Missing delete method
    def deleteFirst(self):
        if not self.isEmpty():
            first = self.getFirst()
            self.setFirst(first.getNext())
            return first.getVal()  # Useful for queue operations

        raise Exception("Cannot delete from an empty list")

    def delete(self, goal, key=getKey):
        if not self.isEmpty():
            current = self.getFirst()
            if goal == key(current.getVal()):
                return self.deleteFirst()

            prev = current
            current = current.getNext()
            while (current):
                if goal == key(current.getVal()):
                    prev.setNext(current.getNext())
                    return current.getVal()

                prev = current
                current = current.getNext()
        else:
            raise Exception("Cannot delete from an empty list")

    def __len__(self):
        n = 0
        current = self.getFirst()
        while (current):
            n += 1
            current = current.getNext()

        return n

    def __repr__(self) -> str:
        current = self.getFirst()
        s = ""
        while (current):
            s += f"{current.getVal()} ->"
            current = current.getNext()
        s += "None\n"
        return s
