from Linked import LinkedList, Node 
import pytest

# test construction of ll
def test_init():
    linked = LinkedList()
    assert linked and isinstance(linked, LinkedList)

def test_insertFront():
    linked = LinkedList()
    assert linked

    linked.insertFront(2)
    assert isinstance(linked.head, Node) and linked.head.data == 2
    
    linked.insertFront(1)
    assert isinstance(linked.head, Node) and linked.head.data == 1

def test_pop():
    linked = LinkedList()
    assert linked
    linked.insertFront(2)
    linked.insertFront(1)
    
    popTwo = linked.pop()
    assert isinstance(popTwo, Node) and popTwo.data == 2

    popOne = linked.pop()
    assert isinstance(popOne, Node) and popOne.data == 1

def test_isValueInList():
    linked = LinkedList()
    assert linked
    retVal = linked.isValueInList(1)
    assert retVal == False
    
    linked.insertFront(2)
    linked.insertFront(1)
    
    retVal = linked.isValueInList(1)
    assert retVal == True

    retVal = linked.isValueInList(100)
    assert retVal == False

def test_getIndex():
    linked = LinkedList()
    assert linked
    retVal = linked.getIndex(-90)
    assert retVal == -1

    linked.insertFront(2)
    linked.insertFront(1)

    retVal = linked.getIndex(1)
    assert retVal == 0

def test_length():
    linked = LinkedList()
    assert linked
    
    # empty list
    retVal = linked.length()
    assert retVal == 0
    
    # 1 element
    linked.insertFront(2)
    retVal = linked.length()
    assert retVal == 1

    # more than one element
    linked.insertFront("TEST")
    retVal = linked.length()
    assert retVal == 2
