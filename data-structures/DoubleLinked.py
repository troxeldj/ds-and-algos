class DLNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def __str__(self):
        return f'{self.data}'

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.len = 0
        
    def insertFront(self, data):
        newNode = DLNode(data)
        if not self.head:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    def pop(self):
        # No nodes
        if not self.head:
            raise Exception("Empty List")
        # One Node
        elif not self.head.next:
            retVal = self.head
            self.head = None
            return retVal
        # 2+ Nodes
        else:
            curr = self.head
            while(curr.next):
                curr = curr.next
            curr.prev.next = curr.next if curr.next else None
            curr.next = None
            curr.prev = None
            return curr
    
    def length(self):
        if not self.head:
            return 0
        else:
            count = 0
            curr = self.head
            while(curr):
                count += 1
                curr = curr.next
            return count

    def printList(self):
        if not self.head:
            print("Empty List")
        else:
            curr = self.head
            while(curr):
                print(f'{curr}', end=" -> ")
                curr = curr.next
            print("None", end="\n")
