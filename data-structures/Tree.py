from collections import dequeue

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = list()
        self.parent = None

    def appendChild(self, node):
        assert isinstance(node, TreeNode)
        node.parent = self
        self.children.append(node)
    
    def isLeaf(self):
        return self.children == 0

    def __str__(self):
        return f'{self.data}'

    def __repr__(self):
        return f'{self.data}'

class Tree:
    def __init__(self):
        self.root = None
        self.nodes = list()
    
    def insert(self, data, parent = None):
        if parent: assert isinstance(parent, TreeNode)
        newNode = TreeNode(data)
        if not self.root:
            self.root = newNode
            self.nodes.append(newNode)
            return
        if parent == None:
            newNode.parent = self.root
            self.root.appendChild(newNode)
        else:
            newNode.parent = parent
            parent.appendChild(newNode)
        self.nodes.append(newNode)

    def getRoot(self):
        return self.root
    

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        newNode = BinaryTreeNode(data)
        if not self.root:
            self.root = newNode
        else:
            self._insert_recursive(data, self.root)

    def _insert_recursive(self, data, cur_node):
        # less than
        if data < cur_node.data:
            # no left child
            if not cur_node.left:
                cur_node.left = newNode
            # has left child 
            else:
                self._insert_recursive(data, cur_node.left)
        # greater than
        elif data > cur_node.data:
            # no right child
            if not cur_node.right:
                cur_node.right = newNode
            # has right child
            else:
                self._insert_recursive(data, cur_node.right)
        # node already exists
        else:
            raise Exception("Node value already exits")

    def inOrder(self, cur_node = None):
        if cur_node == None:
            cur_node = self.root
        if cur_node.left:
           self.inOrder(cur_node.left)
        print(cur_node.data)
        if cur_node.right:
            self.inOrder(cur_node.right)

    def preOrder(self, cur_node = None):
        if cur_node == None:
            cur_node = self.root
        print(cur_node.data)
        if cur_node.left:
           self.preOrder(cur_node.left)
        if cur_node.right:
            self.preOrder(cur_node.right)

    def postOrder(self, cur_node = None):
        if cur_node == None:
            cur_node = self.root
        if cur_node.left:
           self.postOrder(cur_node.left)
        if cur_node.right:
            self.postOrder(cur_node.right)
        print(cur_node.data)

    def breathFirstSearch(value, queue = None, cur_node = None, visited = None):
        # Setup params
        if cur_node == None:
            cur_node = self.root
        if visited == None:
            visited = list()
        if queue == None:
            queue = dequeue()




if __name__ == "__main__":
    # test tree
    print("TEST GENERIC TREE\n")
    tree = Tree()
    tree.insert(2)
    tree.insert(3, tree.getRoot())
    print(tree.nodes)

    # test binary tree
    print("TEST BINARY TREE\n")
    tree = BinaryTree()
    tree.insert(25)
    tree.insert(20)
    tree.insert(15)
    tree.insert(40) 

    print("PREORDER")
    tree.preOrder()

    print("INORDER")
    tree.inOrder()

    print("POSTORDER")
    tree.postOrder()

