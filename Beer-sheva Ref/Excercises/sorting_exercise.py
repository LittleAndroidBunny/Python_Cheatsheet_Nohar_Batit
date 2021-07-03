import numpy as np


def sort_bin(data):
    pivot = 1
    pivot_idx = 0
    for idx, char in enumerate(data):
        if char < pivot:
            data[idx], data[pivot_idx] = data[pivot_idx], data[idx]
            pivot_idx += 1
    return data


unsorted_bin_array = np.random.randint(2, size=(1, 30)).tolist()[0]
print(unsorted_bin_array)
print(sort_bin(unsorted_bin_array))
