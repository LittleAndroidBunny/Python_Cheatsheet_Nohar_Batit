def insertion_sort(l2):
    for i in range(len(l2)):
        Key = l2[i]
        for j in range(len(l2) - 1, i, -1):
            if l2[j] < Key:
                l2[j], l2[j - 1] = l2[j - 1], l2[j]
    return l2


L = [4, 3, 2, 1, 7, 9, 6, -1]
print(insertion_sort(L))
