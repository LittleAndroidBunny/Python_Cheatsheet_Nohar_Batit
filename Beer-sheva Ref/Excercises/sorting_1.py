

def insertion_sort(input_list):
    for i in range(len(input_list)):
        key = input_list[i]
        j = i-1
        while j >= 0 and input_list[j] > key:
            input_list[j + 1] = input_list[j]
            j = j-1
        input_list[j+1] = key


def heap_sort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

        # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)
    return arr


def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)


arr = [12, 11, 13, 5, 6, 1, 10, 32, 43, 25, 21, 17, 30]
heap_sort(arr)
print(arr)

arr = [12, 11, 13, 5, 6, 1, 10, 32, 43, 25, 21, 17, 30]
insertion_sort(arr)
print(arr)


