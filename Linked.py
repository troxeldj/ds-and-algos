class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertFront(self, data):
        newNode: Node = Node(data)
        if not self.head:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
    
    def insertAt(self, index: int, data):
       pass 

    def isValueInList(self, data):
        found = False 
        curr = self.head
        while curr:
            if curr.data == data:
                found = True
            curr = curr.next
        return found

    def pop(self) -> Node:
        if not self.head:
            raise Exception("Empty List")
        elif self.head.next == None:
            self.head = None
        else:
            # Todo
            
            curr = self.head
            newTail = curr
            while(curr.next != None):
                newTail = curr
                curr = curr.next
            retVal = newTail.next
            newTail.next = None
            return retVal

    def printList(self):
        if not self.head:
            print("None")
        else:
            curr:Node = self.head
            while curr != None:
                print(curr.data, end="")
                print(" -> ", end="")
                curr = curr.next
            print("None", end="\n")

    def getIndex(self, data):
        if not self.head:
            return -1
        retInd = -1
        currentInd = 0
        curr = self.head
        while(curr):
            if curr.data == data:
                retInd = currentInd
            currentInd += 1
            curr = curr.next
        return retInd
    
    def length(self):
        if not self.head:
            return 0
        count = 0
        curr = self.head
        while(curr):
            count += 1
            curr = curr.next
        return count


if __name__ == "__main__":
    # Test Creation and print
    linked = LinkedList()
    linked.printList()
    
    # Test Insert
    linked.insertFront(2)
    linked.printList()

    linked.insertFront(4)
    linked.printList()
    
    # Test pop
    linked.pop()
    linked.printList()

    linked.pop()
    linked.printList()
    
    # Test isValueInList
    linked.insertFront(2)
    print(linked.isValueInList(2))
    print(linked.isValueInList(44))
    
    # Test getIndex
    linked.insertFront(1)
    linked.printList()
    print(linked.getIndex(2))
    print(linked.getIndex(1))
    print(linked.getIndex(45))

    # test length
    linked.printList()
    print(linked.length())
    linked.pop()
    print(linked.length())
    linked.pop()
    print(linked.length())
