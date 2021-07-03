import numpy as np
import math


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
    while len(res_lst) < (len(left_lst) + len(right_lst)):
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


unsorted_array = np.random.randint(30, size=(1, 11))
unsorted_array1 = unsorted_array[0].tolist()
unsorted_array2 = unsorted_array1
unsorted_array3 = unsorted_array1

print(unsorted_array1)
print(merge_sort(unsorted_array1))
print(bubble_sort(unsorted_array2))
print(quick_sort(unsorted_array3))
