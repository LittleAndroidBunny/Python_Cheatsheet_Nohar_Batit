import numpy as np
import math
import time
import sys
sys.setrecursionlimit(5000)


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
def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    # use last number as pivot
    pivot = lst[-1]
    left_lst = []
    right_lst = []
    for i in range(len(lst)-1):
        if lst[i] < pivot:
            left_lst.append(lst[i])
        else:
            right_lst.append(lst[i])
    return quick_sort(left_lst) + [pivot] + quick_sort(right_lst)
def merge_sort(lst):
    if len(lst) == 1:
        return lst
    left_lst = merge_sort(lst[:math.ceil(len(lst)/2)])
    right_lst = merge_sort(lst[math.ceil(len(lst)/2):])
    l = 0
    m = 0
    res_lst = []
    while(len(res_lst) < (len(left_lst) + len(right_lst)) ):
        if l < len(left_lst) and m < len(right_lst):
            if left_lst[l] <= right_lst[m]:
                res_lst.append(left_lst[l])
                l += 1
            else:
                res_lst.append(right_lst[m])
                m += 1
        elif l < len(left_lst):
            res_lst.append(left_lst[l])
            l += 1
        else:
            res_lst.append(right_lst[m])
            m += 1

    return res_lst
def bubble_sort(lst):
    for k in range(len(lst)):
        for i in range(len(lst) - 1 - k):
            if lst[i] > lst[i+1]:
                lst[i+1], lst[i] = lst[i], lst[i+1]
    return lst
def insertion_sort(input_list):
    for i in range(len(input_list)):
        key = input_list[i]
        j = i-1
        while j >= 0 and input_list[j] > key:
            input_list[j + 1] = input_list[j]
            j = j-1
        input_list[j+1] = key
    return input_list

def wrapper(arr):
    for func in [quick_sort, merge_sort, bubble_sort, insertion_sort, heap_sort]:
        print(func.__name__)
        t = time.perf_counter()
        result = func(arr.copy())
        print(time.perf_counter() - t)
    print('python_sort')
    t = time.perf_counter()
    arr = arr.copy()
    arr.sort()
    print(time.perf_counter() - t)
    return arr


arr = np.random.randint(3000, size=(1, 3000))
arr = arr[0]
print("different sorting algorithms for a random selected array")
r = wrapper(arr)
print('**********************************************')
print("different sorting algorithms for a sorted array")
r = wrapper(r)
print('**********************************************')
print("different sorting algorithms for a reversed sorted array")
arr = r[-1::-1]
r = wrapper(arr)



