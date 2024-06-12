import random
import timeit
import matplotlib.pyplot as plt


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        current_node = self.head

        if current_node and current_node.data == data:
            self.head = current_node.next
            current_node = None
            return

        prev_node = None
        while current_node and current_node.data != data:
            prev_node = current_node
            current_node = current_node.next

        if current_node is None:
            return

        prev_node.next = current_node.next
        current_node = None

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

    def binary_search(self, num):
        start = self.head
        end = None
        while start:
            end = start
            while end.next:
                end = end.next

            mid = self._get_mid(start, end)

            if mid and mid.data == num:
                return True
            elif mid and mid.data < num:
                start = mid.next
            else:
                end = self._get_previous(start, mid)
                start = end

        return False

    def _get_mid(self, start, end):
        slow = start
        fast = start

        while fast != end and fast.next != end:
            slow = slow.next
            fast = fast.next.next

        return slow

    def _get_previous(self, start, mid):
        current = start
        while current.next != mid:
            current = current.next
        return current


class Array:
    def __init__(self):
        self.array = []

    def append(self, value):
        self.array.append(value)

    def binary_search(self, num):
        low = 0
        high = len(self.array) - 1

        while low <= high:
            mid = (low + high) // 2
            if self.array[mid] == num:
                return True
            elif self.array[mid] < num:
                low = mid + 1
            else:
                high = mid - 1

        return False

def generate_input(size):
    return [random.randint(1, 1000) for elements in range(size)]

def main():
    linked_list = LinkedList()
    array = Array()
    inputs_size = [1000,2000,4000,8000]
    y_ll = []
    y_arr = []
    
    for i in inputs_size:
        inputs = generate_input(i)
        for element in inputs:
            linked_list.append(i)
            array.append(i)
        
        ll_mid = linked_list._get_mid
        
        elapsed_time_ll = timeit.timeit(lambda: linked_list.binary_search(i/2), number=1)
        elapsed_time_arr = timeit.timeit(lambda: array.binary_search(), number=1)

        y_ll.append(elapsed_time_ll)
        y_arr.append(elapsed_time_arr)
    
    print(y_ll)
    print(y_arr)
    plt.plot(inputs_size, y_ll, label='LinkedList Binary Search')
    plt.plot(inputs_size, y_arr, label='Array Binary Search')
    plt.xlabel('Size of Inputs')
    plt.ylabel('Time (seconds)')
    plt.title('LinkedLists Binary Search vs Array Binary Search Performance')
    plt.legend()

    plt.show()




# Example usage:
if __name__ == "__main__":
    main()

