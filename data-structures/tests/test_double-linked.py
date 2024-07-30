from DoubleLinked import DoublyLinkedList, DLNode
import pytest

def test_construction():
    dll = DoublyLinkedList()
    assert dll and isinstance(dll, DoublyLinkedList)

def test_insertFront():
    dll = DoublyLinkedList()
    assert dll

    # 1 element
    dll.insertFront(2)
    assert isinstance(dll.head, DLNode) and dll.head.data == 2
    
    # 2 elements
    dll.insertFront(3)
    assert isinstance(dll.head, DLNode) and dll.head.data == 3
    assert dll.head.next and dll.head.next.data == 2 and dll.head.next.prev.data == 3

def test_pop():
    dll = DoublyLinkedList()

    # empty list
    with pytest.raises(Exception):
        dll.pop()

    # 1 element
    dll.insertFront(5)
    retVal = dll.pop()
    assert dll.length() == 0 and retVal.data == 5

    # 2 elements
    dll.insertFront(5)
    dll.insertFront(8)
    dll.pop()
    assert dll.length() == 1 and retVal.data == 5

def test_length():
    # empty list
    dll = DoublyLinkedList()
    assert dll.length() == 0

    # 1 element
    dll.insertFront(23)
    assert dll.length() == 1

    # 2 elements
    dll.insertFront(59)
    assert dll.length() == 2
