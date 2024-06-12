import timeit
import numpy as np
import matplotlib.pyplot as plt

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)

def bubblesort(elements):
    elements = elements.copy()  # Ensure that the original array is not modified
    n = len(elements)
    for i in range(n-1):
        swapped = False
        for j in range(0, n-i-1):
            if elements[j] > elements[j+1]:
                elements[j], elements[j+1] = elements[j+1], elements[j]
                swapped = True
        if not swapped:
            break
    return elements

def main():
    y_bubble_average = []
    y_bubble_best = []
    y_bubble_worst = []

    y_quick_average = []
    y_quick_best = []
    y_quick_worst = []
    sizes = list(range(1, 21,1))  # Adjust this range according to your needs
    for size in sizes:
        random_array = np.random.randint(100, size=size)
        sorted_array = sorted(random_array)
        reversed_array = sorted(random_array, reverse=True)

        # Generate worst case scenario (descending order)
        worst_case_array = list(range(size, 0, -1))

        elapsed_time_bubble_avg = timeit.timeit(lambda: bubblesort(random_array.copy()), number=1000)
        elapsed_time_bubble_bst = timeit.timeit(lambda: bubblesort(sorted_array.copy()), number=1000)
        elapsed_time_bubble_wst = timeit.timeit(lambda: bubblesort(worst_case_array.copy()), number=1000)

        elapsed_time_quick_avg = timeit.timeit(lambda: quicksort(random_array.copy()), number=1000)
        elapsed_time_quick_bst = timeit.timeit(lambda: quicksort(sorted_array.copy()), number=1000)
        elapsed_time_quick_wst = timeit.timeit(lambda: quicksort(worst_case_array.copy()), number=1000)
        
        y_bubble_best.append(elapsed_time_bubble_bst)
        y_bubble_average.append(elapsed_time_bubble_avg)
        y_bubble_worst.append(elapsed_time_bubble_wst)        

        y_quick_best.append(elapsed_time_quick_bst)
        y_quick_average.append(elapsed_time_quick_avg)
        y_quick_worst.append(elapsed_time_quick_wst)

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 3, 1)
    plt.plot(sizes, y_bubble_best, label='Bubble Sort Best Case')
    plt.plot(sizes, y_quick_best, label='Quick Sort Best Case')
    plt.xlabel('Size of Array')
    plt.ylabel('Time (seconds)')
    plt.title('Bubble Sort Best Case')
    plt.legend()

    plt.subplot(1, 3, 2)
    plt.plot(sizes, y_bubble_average, label='Bubble Sort Average Case')
    plt.plot(sizes, y_quick_average, label='Quick Sort Average Case')
    plt.xlabel('Size of Array')
    plt.ylabel('Time (seconds)')
    plt.title('Bubble Sort Average Case')
    plt.legend()

    plt.subplot(1, 3, 3)
    plt.plot(sizes, y_bubble_worst, label='Bubble Sort Worst Case')
    plt.plot(sizes, y_quick_worst, label='Quick Sort Worst Case')
    plt.xlabel('Size of Array')
    plt.ylabel('Time (seconds)')
    plt.title('Bubble Sort Worst Case')
    plt.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
