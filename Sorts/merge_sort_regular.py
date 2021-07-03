# Python program for implementation of MergeSort
def mergeSort(arr1):
    if len(arr1) > 1:
        mid = len(arr1) // 2  # Finding the mid of the array
        L = arr1[:mid]  # Dividing the array elements
        R = arr1[mid:]  # into 2 halves

        mergeSort(L)  # Sorting the first half
        mergeSort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr1[k] = L[i]
                i += 1
            else:
                arr1[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr1[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr1[k] = R[j]
            j += 1
            k += 1


# Code to print the list
def printList(arr2):
    for i in range(len(arr2)):
        print(arr2[i], end=" ")
    print()


# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
    # Time complexity O(n*log n)
    #space complexity (not learned) O(n)