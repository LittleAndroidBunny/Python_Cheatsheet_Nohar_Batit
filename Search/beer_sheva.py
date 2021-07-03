def naive_search(arr,value):
    for idx, num in enumerate(arr):
        if num == value:
            print('found it! index= {}'.format(idx))
            break
    return idx


def binary_search(arr, value):
    # Check base case
    if not(len(arr)):
        return 0

    if arr[int(len(arr)/2)] == value:
        return int(len(arr)/2)

    if arr[int(len(arr)/2)] > value:
        return binary_search(arr[:int(len(arr)/2)-1], value)

    return binary_search(arr[int(len(arr) / 2)+1:], value) + int(len(arr) / 2) + 1


arrr = [12, 11, 13, 5, 6, 1, 10, 32, 43, 25, 21, 17, 30]
value = 25
key = naive_search(arrr, value)
print(key)
key = binary_search(arrr, value)
print(key)
