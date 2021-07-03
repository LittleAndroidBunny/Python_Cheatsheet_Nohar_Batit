
def mult_by_param(num):
    return lambda param: (param ** 2) * num


def main_func():

    # can be used for inline functions:
    x = lambda num: num * 2
    print(x(10))
    print(type(x))

    # Lambda functions can have several arguments:
    x = lambda x, y, z: x* y + z
    print(x(10, 2, 3))
    print(type(x))

    # can be used as a way to send parameters to functions
    multiply_by_3 = mult_by_param(3)
    multiply_by_5 = mult_by_param(5)

    print(multiply_by_3(10))
    print(multiply_by_5(10))
    print(mult_by_param(3)(5))

    # functions can also be assigned to tags:
    x = print
    x('Hello World!')
    print(type(x))
    print(x)
    x(print)


if __name__ == '__main__':
    main_func()
    print(type(main_func))
