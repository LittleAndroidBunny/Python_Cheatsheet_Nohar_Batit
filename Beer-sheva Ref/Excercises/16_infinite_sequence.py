def infinite_sequence():
    num = 1
    while True:
        yield num
        num *= 2


for i in infinite_sequence():
    print(i, end=" ")
    if i > 1000000:
        break
