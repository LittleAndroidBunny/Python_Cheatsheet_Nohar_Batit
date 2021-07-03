def example4(n, k):
    if n < k:
        return 0
    if (k == 1) | (n-k == 1):
        return n
    if k == n:
        return 1
    return example4(n-1, k-1) + example4(n-1, k)

print(example4(4, 2))
