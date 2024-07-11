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
    
    popOne = linked.pop()
    assert isinstance(popOne, Node) and popOne.data == 1

    popTwo = linked.pop()
    assert isinstance(popTwo, Node) and popTwo.data == 2


