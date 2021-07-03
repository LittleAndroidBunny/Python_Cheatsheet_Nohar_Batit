def sum_series(num):
    if num < 0:
        return 0
    return num + sum_series(num - 2)

print(sum_series(10))