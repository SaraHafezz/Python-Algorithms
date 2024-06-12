import random
import timeit

class Variable:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

class PriorityQueue:
    space = [None] * 100000
    size = -1

class PriorityQueue:
    space = [None] * 100000
    size = -1

    @classmethod
    def enqueue(cls, value, priority):
        if priority > 7 or priority < 0:
            return  # Consider handling invalid priority gracefully

        cls.size += 1
        cls.space[cls.size] = Variable(value, priority)
        cls._merge_sort(0, cls.size)  # Sort the array after adding the item

    @classmethod
    def _merge_sort(cls, low, high):
        if low < high:
            mid = (low + high) // 2
            cls._merge_sort(low, mid)
            cls._merge_sort(mid + 1, high)
            cls._merge(low, mid, high)

    @classmethod
    def _merge(cls, low, mid, high):
        left_half = cls.space[low:mid + 1]
        right_half = cls.space[mid + 1:high + 1]

        left_index = right_index = 0
        merged_index = low

        while left_index < len(left_half) and right_index < len(right_half):
            if left_half[left_index].priority <= right_half[right_index].priority:
                cls.space[merged_index] = left_half[left_index]
                left_index += 1
            else:
                cls.space[merged_index] = right_half[right_index]
                right_index += 1
            merged_index += 1

        while left_index < len(left_half):
            cls.space[merged_index] = left_half[left_index]
            left_index += 1
            merged_index += 1

        while right_index < len(right_half):
            cls.space[merged_index] = right_half[right_index]
            right_index += 1
            merged_index += 1

    @classmethod
    def dequeue(cls):
        if cls.size == -1:
            print("Priority queue is empty.")
            return None

        highest_priority_index = 0
        for i in range(1, cls.size + 1):
            if cls.space[i].priority > cls.space[highest_priority_index].priority:
                highest_priority_index = i

        highest_priority_item = cls.space[highest_priority_index]

        for i in range(highest_priority_index, cls.size):
            cls.space[i] = cls.space[i + 1]

        cls.space[cls.size] = None
        cls.size -= 1

        return highest_priority_item


class PriorityQueue2:
    space = [None] * 100000
    size = -1

    @classmethod
    def dequeue(cls):
        if cls.size == -1:
            print("Priority queue is empty.")
            return None

        highest_priority_index = 0
        for i in range(1, cls.size + 1):
            if cls.space[i].priority > cls.space[highest_priority_index].priority:
                highest_priority_index = i

        highest_priority_item = cls.space[highest_priority_index]

        for i in range(highest_priority_index, cls.size):
            cls.space[i] = cls.space[i + 1]

        cls.space[cls.size] = None
        cls.size -= 1

        return highest_priority_item
    
    @classmethod
    def enqueue(cls, value, priority):
        if priority > 7 or priority < 0:
            return

        insert_index = cls.size
        while insert_index >= 0 and cls.space[insert_index].priority < priority:
            cls.space[insert_index + 1] = cls.space[insert_index]
            insert_index -= 1

        cls.space[insert_index + 1] = Variable(value, priority)
        cls.size += 1


def random_tasks():
    tasks = []
    for _ in range(1000):
        if random.random() < 0.7:
            tasks.append(('enqueue', random.randint(1, 100)))
        else:
            tasks.append(('dequeue', None))
    return tasks


def simulate_pq(pq_type, tasks):

    if pq_type == 'PriorityQueue':
        pq = PriorityQueue()
        for task, value in tasks:
            if task == 'enqueue':
                pq.enqueue(value, random.randint(0, 6))
            elif task == 'dequeue':
                pq.dequeue()

    elif pq_type == 'PriorityQueue2':
        pq = PriorityQueue2()
        for task, value in tasks:
            if task == 'enqueue':
                pq.enqueue(value, random.randint(0, 6))
            elif task == 'dequeue':
                pq.dequeue()

    else:
        print("Invalid priority queue type")
        return


def main():
    tasks = random_tasks()
    pq = 'PriorityQueue'
    pq2 = 'PriorityQueue2'
    PQ = 0
    PQ2 = 0
    for i in range(100):
        PQ = timeit.timeit(lambda: simulate_pq(pq, tasks), number=100)
        PQ2 = timeit.timeit(lambda: simulate_pq(pq2, tasks), number=100)
        elapsed_time_PQ += PQ
        elapsed_time_PQ2 += PQ2
    print("The first implementation of the PriorityQueue has a runtime of ", elapsed_time_PQ," seconds.")
    print("The second implementation of the PriorityQueue has a runtime of ", elapsed_time_PQ2," seconds.")

if __name__ == "__main__":
    main()

'''
The second implementation of a Prioirty Queue is superior in time complexity. This is due to the sorting in the first
implementation. Basically, for the first implementtion every enqueue is a longer process due to having to sort, thus
resulting in a best case scenario of O(n). Where as, for the second case scenario the average to worst case scenario is
O(n) since the enqueue traverses the list to find the appropriate insertion point.
'''