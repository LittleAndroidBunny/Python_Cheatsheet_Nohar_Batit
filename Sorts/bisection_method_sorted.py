def bisect_search_sorted(l1, e):
    if not l1:
        return False
    elif len(l1) == 1:
        return l1[0] == e
    else:
        half = len(l1) // 2
        if l1[half] > e:
            return bisect_search_sorted(l1[:half], e)
        else:
            return bisect_search_sorted(l1[half:], e)


L = [3, 56, 4, 9, 8, 4, 956, 6, 12, 5, 6, 98, 4, 32, 56, 48, 12, 68, 87]
print(bisect_search_sorted(sorted(L), 98))
