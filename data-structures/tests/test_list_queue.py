from Queue import ListQueue

def test_construction():
    queue = ListQueue()
    assert queue


def test_isEmpty():
    queue = ListQueue()
    assert queue
    
    # empty list
    assert queue.isEmpty() == True

    # 1 element
    queue.enqueue(2)
    assert queue.isEmpty() == False

    # multiple elements
    queue.enqueue(18)
    assert queue.isEmpty() == False

def test_enqueue():
    queue = ListQueue()
    
    # 1 element
    queue.enqueue(1)
    assert queue.isEmpty() == False and queue._items[0] == 1

    # multiple elements
    queue.enqueue(2)
    assert queue.isEmpty() == False
    assert queue._items[0] == 1 and queue._items[1] == 2

def test_dequeue():
    

def test_peek():
    pass

