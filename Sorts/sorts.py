import random
import time


def checkDifferentTime(num1, num2):
    if (num1 > num2):
        return ((num2 / num1) * 100)
    else:
        return ((num1 / num2) * 100)


def printArray(arr, name):
    if (name == 'Bubble'):
        print('Sort array from Bubble Sort Sorted array is:')
    elif (name == 'Insertion'):
        print('Sort array from Insertion Sort Sorted array is:')
    elif (name == 'Selection'):
        print('Sort array from Selection Sort Sorted array is:')
    elif (name == 'Quick'):
        print('Sort array from Quick Sort Sorted array is:')
    elif (name == 'Merge'):
        print('Sort array from Merge Sort Sorted array is:')
    elif (name == 'Heap'):
        print('Sort array from Heap Sort Sorted array is:')
    for i in range(len(arr)):
        print(arr[i], end=' ')
    print("")


def CheckTime(nameFunc, startTime):
    elapsedTime = time.time() - startTime
    print('function [{}] finished in {:.3f} sec'.format(
        nameFunc.__name__, float(elapsedTime)))  # sec to ms --> 1000 * time
    return elapsedTime


# To heapify subtree rooted at index i.
# n is size of heap
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2
    count = 0
    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l
        count += 1
        # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r
        count += 1
        # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        count += 1
        # Heapify the root.
        heapify(arr, n, largest)
    return count


# Function to do heap sort
def heapSort(arr):
    n = len(arr)
    count = 0
    # Build a maxheap.
    for i in range(n, -1, -1):
        count += 1
        count += heapify(arr, n, i)

        # One by one extract elements
    for i in range(n - 1, 0, -1):
        count += 1
        arr[i], arr[0] = arr[0], arr[i]  # swap
        count += heapify(arr, i, 0)
    # print("Number of operations / complications of the function heap sort --- O(n_Log_n): ", count)


# Function to do merge sort
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        mergeSort(L)  # Sorting the first half
        mergeSort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):
        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index
def quickSortHelper(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSortHelper(arr, low, pi - 1)
        quickSortHelper(arr, pi + 1, high)


# Function to do Quick sort
def quickSort(arr):
    quickSortHelper(arr, 0, len(arr) - 1)


# Function to do selection sort
def selectionSort(arr):
    count = 0
    for i in range(len(arr)):
        count += 1
        # Find the minimum element in remaining
        # unsorted array
        min_index = i
        for j in range(i + 1, len(arr)):
            count += 1
            if arr[min_index] > arr[j]:
                min_index = j
                # Swap the found minimum element with
        # the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    # print("Number of operations / complications of the function selection sort -- O(n^2): ", count)


# Function to do insertion sort
def insertionSort(arr):
    count = 0  ####
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            count += 1  #####
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        count += 1  #####
    # print("Number of operations / complications of the function insertion sort -- O(n^2): ", count)


# Function to do bubble sort
def bubbleSort(arr):
    n = len(arr)
    count = 0  # count operation of func
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            count += 1  ####
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        count += 1  ####
    # print("Number of operations / complications of the function bubble sort -- O(n^2): ", count)


# Code to test

# Crate the array numbers with random number..
arrayBubbleSort = []
arrayInsertionSort = []
arraySelectionSort = []
arrayQuickSort = []
arrayMergeSort = []
arrayHeapSort = []

# Bubble sort create
for _ in range(10000):
    arrayBubbleSort.append(random.randint(1, 500))
print("----- Array Random 1 --- Bubble sort: ---- ")
for i in range(len(arrayBubbleSort)):
    print(arrayBubbleSort[i], end=' ')
print("")

# Insertion sort create
for _ in range(10000):
    arrayInsertionSort.append(random.randint(1, 500))
print("---- Array Random 2 ---- insertion sort: ----")
for i in range(len(arrayInsertionSort)):
    print(arrayInsertionSort[i], end=' ')
print("")

# Selection sort create
for _ in range(10000):
    arraySelectionSort.append(random.randint(1, 500))
print(" ---- Array Random 3 --- Selection Sort: ---- ")
for i in range(len(arraySelectionSort)):
    print(arraySelectionSort[i], end=' ')
print("")

# Quick sort create
for _ in range(10000):
    arrayQuickSort.append(random.randint(1, 5000))
print("----- Array Random 4 --- Quick sort: ---- ")
for i in range(len(arrayQuickSort)):
    print(arrayQuickSort[i], end=' ')
print("")

# Merge sort create
for _ in range(10000):
    arrayMergeSort.append(random.randint(1, 5000))
print("----- Array Random 5 --- Merge sort: ---- ")
for i in range(len(arrayMergeSort)):
    print(arrayMergeSort[i], end=' ')
print("")

# Heap sort create
for _ in range(10000):
    arrayHeapSort.append(random.randint(1, 5000))
print("----- Array Random 6 --- Heap sort: ---- ")
for i in range(len(arrayHeapSort)):
    print(arrayHeapSort[i], end=' ')
print("")

print(" ")
# Do & Check how much time it is -- bubble sort
startTime = time.time()
bubbleSort(arrayBubbleSort)
bubbleTime = CheckTime(bubbleSort, startTime)
print(" ")
# Do &Check how much time it is -- insertion sort
startTime = time.time()
insertionSort(arrayInsertionSort)
insertionTime = CheckTime(insertionSort, startTime)
print(" ")
# Do &Check how much time it is -- Selection sort
startTime = time.time()
selectionSort(arraySelectionSort)
selectionTime = CheckTime(selectionSort, startTime)
print(" ")
# Do & Check how much time it is -- quick sort
startTime = time.time()
quickSort(arrayQuickSort)
quickTime = CheckTime(quickSort, startTime)
print(" ")
# Do & Check how much time it is -- merge sort
startTime = float(time.time())
mergeSort(arrayMergeSort)
mergeTime = CheckTime(mergeSort, startTime)
print(" ")
# Do & Check how much time it is -- heap sort
startTime = time.time()
heapSort(arrayHeapSort)
heapTime = CheckTime(heapSort, startTime)
print(" ")

# print("The difference between insertion sort to bubble sort is: {:.1f}%".format(checkDifferentTime(insertionTime,
# bubbleTime)))
print(" ")
# Print the test..
printArray(arrayBubbleSort, 'Bubble')
printArray(arrayInsertionSort, 'Insertion')
printArray(arraySelectionSort, 'Selection')
printArray(arrayQuickSort, 'Quick')
printArray(arrayMergeSort, 'Merge')
printArray(arrayHeapSort, 'Heap')
