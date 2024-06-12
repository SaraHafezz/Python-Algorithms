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
        elif key > root.key:
            root.right = self._insert_recursive(root.right, key)
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

    # Insert integers from 1 to 1000 into the binary search tree
    for i in range(1, 1001):
        bst.insert(i)

    # Generate random search tasks
    search_tasks = generate_random_search_tasks()

    # Measure performance
    search_times, max_balances = measure_performance(bst, search_tasks)

    # Generate scatterplot
    plt.scatter(max_balances, search_times)
    plt.xlabel('Absolute Balance')
    plt.ylabel('Search Time (seconds)')
    plt.title('Balance vs. Search Time')
    plt.show()
