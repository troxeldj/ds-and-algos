class ListStack:
    def __init__(self):
        self._stack = list()

    def isEmpty(self) -> int:
        return len(self._stack) == 0
    
    def push(self, data) -> None:
        self._stack.append(data)

    def pop(self):
        if self.isEmpty():
            raise Exception('Empty Stack')
        else:
            self._stack.pop()

    def length(self):
        return len(self._stack)

    def printStack(self):
        if self.isEmpty():
            print('Empty Stack')
            return
        for i in reversed(range(self.length())):
            print(self._stack[i], end=" -> ")
        print("", end="\n")

class LLStackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f'{self.data}'

class LinkedListStack:
    def __init__(self):
        self.top = None
        self.length = 0

    def isEmpty(self):
        return self.length == 0
    
    def push(self, data):
        newNode = LLStackNode(data)
        # No nodes
        if self.isEmpty():
            self.top = newNode
        # 1+ nodes 
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1

    def pop(self):
        # no nodes
        if self.isEmpty():
            raise Exception("Empty Stack")
        # 1 node
        elif not self.head.next:
            retVal = self.head
            self.head = None
            self.length += 1
            return retVal
        # 2+ nodes
        else:
            curr = self.head
            newTail = curr
            while(curr.next != None):
                newTail = curr
                curr = curr.next
            retVal = newTail.next
            newTail.next = None
            self.length += 1
            return retVal

    def peek(self):
        if self.isEmpty(): return None
        return self.top

    def length(self):
        return self.length
