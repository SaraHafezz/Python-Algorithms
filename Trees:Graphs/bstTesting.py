import random
import time
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(10000)  # Change 10000 to the desired recursion limit

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.balance = 0
        self.parent = None 


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, root, key):
        if root is None:
            return TreeNode(key)
        
        if key < root.key:
            root.left = self._insert_recursive(root.left, key)
            root.balance += 1
        elif key > root.key:
            root.right = self._insert_recursive(root.right, key)
            root.balance -= 1

        # Check for pivot node
        pivot_node = self._get_pivot_node_recursive(self.root)
        if pivot_node is None:
            print("Case #1: Pivot not detected")
        else:
            if root == pivot_node:
                print("Case #2: A pivot exists, and a node was added to the shorter subtree")
            root.balance = self._get_balance_recursive(root)
        
        return root

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._search_recursive(root.left, key)
        return self._search_recursive(root.right, key)

    def get_balance(self):
        return self._get_balance_recursive(self.root)

    def _get_balance_recursive(self, root):
        if root is None:
            return 0
        return self._height(root.left) - self._height(root.right)

    def _height(self, node):
        if node is None:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))
    
    def _get_pivot_node_recursive(self, root):
        if root is None:
            return None
        balance = self._get_balance_recursive(root)
        if abs(balance) > 1:
            return root
        left_pivot = self._get_pivot_node_recursive(root.left)
        right_pivot = self._get_pivot_node_recursive(root.right)
        if left_pivot:
            return left_pivot
        if right_pivot:
            return right_pivot
        return None
    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left is not None:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right is not None:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, root, key):
        if root is None:
            return TreeNode(key)

        if key < root.key:
            root.left = self._insert_recursive(root.left, key)
            root.balance += 1
        elif key > root.key:
            root.right = self._insert_recursive(root.right, key)
            root.balance -= 1

        pivot_node = self._get_pivot_node_recursive(self.root)
        if pivot_node is None:
            print("Case #1: Pivot not detected")
        else:
            if root == pivot_node:
                if root.balance > 1:
                    print("Case #3a: Adding a node to an outside subtree")
                    if key < root.left.key:
                        self._right_rotate(root)
                    else:
                        self._left_rotate(root.left)
                        self._right_rotate(root)
                elif root.balance < -1:
                    print("Case #3b not supported")
                    # You can handle case 3B here
                root.balance = self._get_balance_recursive(root)

        return root

def generate_random_search_tasks():
    integers = list(range(1, 1001))
    random.shuffle(integers)
    return integers

def measure_performance(tree, tasks):
    search_times = []
    max_balances = []
    for task in tasks:
        start_time = time.time()
        tree.search(task)
        end_time = time.time()
        search_times.append(end_time - start_time)
        max_balances.append(abs(tree.get_balance()))
    return search_times, max_balances

if __name__ == "__main__":
    bst = BinarySearchTree()

    # Test Case 1: Adding a node results in case 1
    print("Test Case 1:")
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)

    # Test Case 2: Adding a node results in case 2
    print("\nTest Case 2:")
    bst = BinarySearchTree()  # Reset the tree
    bst.insert(5)
    bst.insert(7)
    bst.insert(6)

    # Test Case 3: Adding a node results in case 3 (the code should print “Case 3 not supported”)
    print("\nTest Case 3:")
    bst = BinarySearchTree()
    bst.insert(3)
    bst.insert(2)
    bst.insert(1)
    print("\nTest Case 3b not supported")
