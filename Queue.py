class LLQueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListQueue:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def length(self):
        return self.size

    def isEmpty(self):
        return self.size == 0
    
    def enqueue(self, data):
        newNode = LLQueueNode(data)
        if self.isEmpty():
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode
        self.size += 1
    
    def printQueue(self):
        if self.isEmpty():
            print("Empty List")
        else:
            curr = self.top
            while(curr):
                print(curr.data, end=" -> ")
                curr = curr.next
            print("", end="\n")
    
    def dequeue(self):
        if self.isEmpty():
            raise Exception("Empty Queue")
        elif not self.top.next:
            retVal = self.top
            self.top = None
            self.size -= 1
            return retVal
        else:
            curr = self.top
            newTail = curr
            while(curr.next != None):
                newTail = curr
                curr = curr.next
            retVal = newTail.next
            newTail.next = None
            self.size -= 1
            return retVal

class ListQueue:
    def __init__(self):
        self._items = list()
        self.size = 0

    def length(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def enqueue(self, data):
        self._items.append(data)
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            raise Exception('Empty Queue')
        self._items.pop(0)
        self.size -= 1

    def peek(self):
        if self.isEmpty():
            return None
        return self._items[0]

    def printQueue(self):
        if self.isEmpty():
            print('Empty Queue')
            return
        for i in range(self.length()):
            print(self._items[i], end=" -> ")
        print("")
        


if __name__ == "__main__":
    # Test creation, size, print
    print("TESTING QUEUE (LIST IMPLEMENTATION)", end="\n\n")
    listQueue = ListQueue()
    print(listQueue.length())
    listQueue.printQueue()

    # Test enqueue
    listQueue.enqueue(2)
    print(listQueue.length())
    listQueue.printQueue()
    listQueue.enqueue(3)
    print(listQueue.length())
    listQueue.printQueue()
    
    # Test dequeue
    listQueue.dequeue()
    print(listQueue.length())
    listQueue.printQueue()
    listQueue.dequeue()
    print(listQueue.length())
    listQueue.printQueue()


    # Test Linked List queue
    print("TESTING QUEUE (LINKED LIST IMPLEMENTATION)", end="\n\n")
    linkedLQueue = LinkedListQueue()
    print(linkedLQueue.length())
    linkedLQueue.printQueue()

    linkedLQueue.enqueue(2)
    print(linkedLQueue.length())
    linkedLQueue.printQueue()

    linkedLQueue.enqueue(3)
    print(linkedLQueue.length())
    linkedLQueue.printQueue()

    linkedLQueue.dequeue()
    print(linkedLQueue.length())
    linkedLQueue.printQueue()

    linkedLQueue.dequeue()
    print(linkedLQueue.length())
    linkedLQueue.printQueue()


