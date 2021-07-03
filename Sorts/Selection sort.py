### selection sort :

def selection_sort(l):
    c = 0
    for a in range(len(l)):
        for b in range(a, len(l)):
            c += 1
            if l[a] > l[b] and b > a:
                l[a], l[b] = l[b], l[a]

    print(c)
    return l


L = [9, 5, 6, -5, 36, 98, 75, 42, 15, 18, 46, 13, 39, 3, 5, 4, 8, 85]
print(selection_sort(L))

# complexity is : n^2-C = O(n^2) - quadratic
