# O(c)
def constant_algo(items):
    result = items[0] * items[0]
    print()


constant_algo([4, 5, 6, 8])


#######################################################

# O(n)
def linear_algo(items):
    for item in items:
        print(item)


linear_algo([4, 5, 6, 8])


#######################################################

def linear_algo(items):
    for item in items:
        print(item)

    for item in items:
        print(item)


linear_algo([4, 5, 6, 8])


# O(2n) -- < O(n)
#######################################################

# O(n^2)

def quadratic_algo(items):
    for item in items:
        for item2 in items:
            print(item, ' ', item)


quadratic_algo([4, 5, 6, 8])


#######################################################

def complex_algo(items):
    for i in range(5):  # O(5)
        print("Python is awesome")

    for item in items:  # O(n)
        print(item)

    for item in items:  # O(n)
        print(item)

    print("Big O")  # O(1)
    print("Big O")  # O(1)
    print("Big O")  # O(1)


complex_algo([4, 5, 6, 8])


# O(5) + O(n) + O(n) + O(3) = O(8) + O(2n) -- > O(n).

#######################################################

def search_algo(num, items):
    for item in items:
        if item == num:
            return True
        else:
            return False


nums = [2, 4, 6, 8, 10]

print(search_algo(2, nums))


# Best - O(1)
# Worst - O(n)
# Find if a number is even or odd.

#######################################################
def isEvenOrOdd(n):
    return n % 2


# O(1) - O(n)

#######################################################

# Bubble Sort O(n^2)

def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)


#######################################################
# It returns index of x in given array arr if present,
# else returns -1
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
        # means x is present at mid
        else:
            return mid
    # If we reach here, then the element was not present
    return -1


# Test array
arr = [2, 3, 4, 10, 40]
x = 10

result = binary_search(arr, x)
print(result)   