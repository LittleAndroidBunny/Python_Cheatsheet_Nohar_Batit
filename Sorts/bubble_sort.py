### bubble sort :

def bubble(l1):
    if not l1:
        return "This is an empty list"
    flag = True
    while flag:
        flag = False
        for i in range(len(l1) - 1):
            if l1[i] > l1[i + 1]:
                temp = l1[i]
                l1[i] = l1[i + 1]
                l1[i + 1] = temp
                flag = True

    return l1


L = [1, 2, 9, 6, 5, 9, 6, 2, 1, 4, 5, 78, 45, 12, 29, 85, 64, 32, 18, 72]
print(bubble(L))

# Program Complexity is : O(n^2)
