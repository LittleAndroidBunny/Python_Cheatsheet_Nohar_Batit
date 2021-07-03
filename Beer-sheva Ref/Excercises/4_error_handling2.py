def divide_numbers_safe():
    while True:
        try:
            d = input('Please enter the denominator: ')
            n = input('Please enter the numerator: ')
            print('The result is: ' + str(int(n)/int(d)))
            return
        except ValueError:
            print("\nPlease enter a number!! \n")


def divide_numbers_safer():
    while True:
        try:
            d = input('Please enter the denominator: ')
            n = input('Please enter the numerator: ')
            print('The result is: ' + str(int(n)/int(d)))
            return
        except ValueError:
            print("\nPlease enter a number!! \n")
        except ZeroDivisionError:
            print("\nDenominator can't be zero!! \n")


def main():
    divide_numbers_safe()


if __name__ == '__main__':
    main()
