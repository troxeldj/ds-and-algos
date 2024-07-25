#include "linked.h"
#include <iostream>

template <typename T>
LinkedList<T>::LinkedList() {
  head = nullptr;
  size = 0;
}

template <typename T>
void LinkedList<T>::insert(T data) {
  Node<T> newNode = Node(data);
  if(isEmpty()) {
    head = newNode;
  } else {
    newNode.next = head;
    head = newNode;
  }
  size++;
}

template <typename T>
void LinkedList<T>::printList() {
  // no nodes
  if(isEmpty()){
    std::cout << "empty list.\n";
    return;
  }
  // we have at least one node
  Node<T>* curr = head;
  while(curr != nullptr) {
    std::cout << curr->data << " ";
  }
  std::cout << "\n";
}

template <typename T>
bool LinkedList<T>::isEmpty() {
  return size <= 0;
}
