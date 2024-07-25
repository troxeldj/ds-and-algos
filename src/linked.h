

template <typename T>
struct Node {
public:
  T data;
  Node* next;

  Node(T val) {
    data = val;
  }

};

template <typename T>
class LinkedList {
private:
  Node<T>* head;
  int size; 
public:
  //constructor
  LinkedList();

  // operations
  void insert(T data);
  void printList();
  bool isEmpty();
private:
};
