import sys 
sys.setrecursionlimit(20000)

def merge_sort(arr,low,high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        merge(arr,low,mid,high)

def merge(arr, low, mid, high):
    # Create temporary arrays to hold the two halves
    left_half = arr[low:mid+1]
    right_half = arr[mid+1:high+1]

    # Initialize pointers for left_half, right_half, and the main array
    left_index = 0
    right_index = 0
    merged_index = low

    # Merge the temp arrays back into arr[low..high]
    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] <= right_half[right_index]:
            arr[merged_index] = left_half[left_index]
            left_index += 1
        else:
            arr[merged_index] = right_half[right_index]
            right_index += 1
        merged_index += 1

    # Copy the remaining elements of left_half, if there are any
    while left_index < len(left_half):
        arr[merged_index] = left_half[left_index]
        left_index += 1
        merged_index += 1

    # Copy the remaining elements of right_half, if there are any
    while right_index < len(right_half):
        arr[merged_index] = right_half[right_index]
        right_index += 1
        merged_index += 1

test_array = [8,42,25,3,3,2,27,3]

merge_sort(test_array,0,len(test_array)-1)

print(test_array)