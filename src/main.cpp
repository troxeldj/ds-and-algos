#include <iostream>
#include "linked.h"

int main() {
  LinkedList<int> ll = LinkedList<int>();
  ll.printList();

  ll.insert(4);
  ll.printList();

  ll.insert(5);
  ll.printList();
}
