# This script is part of tutorial number 3 of introduction of computer science for EE students at BGU.
# Topics, Comprehensive review of:
#   - loops
#   - conditionals
#   - strings
#   - introduce the input function

# taking user input
# usr_input_str = input("Please enter a value: ")


# testing for a legitimate password
minimal_length = 10  # minimal allowed length
while True:
    # prompt user for input
    usr_str = input("Please enter a password:")

    length_test = None
    upper_case_test = None
    lower_case_test = None
    digit_test = None
    repeat_test = 1  # why is this initialized as one
    alpha_numeric_test = 1  # why is this initialized as one

    if len(usr_str) < minimal_length:  # test minimal length
        print("Password should be at least " + str(minimal_length) + \
              " characters long.")
    else:
        length_test = 1
        for i in range(0, len(usr_str)):
            if i < len(usr_str)-2:  # test repeating chars
                if usr_str[i] == usr_str[i+1] and usr_str[i] == usr_str[i+2]:
                    repeat_test = 0
                    print("Can't use repeating characters.")
                    break  # what loop does it break

            if usr_str[i].isdigit():  # digit test
                if not digit_test:
                    digit_test = 1
                continue  # Where does this take me

            if usr_str[i].isupper():  # upper case test
                if not upper_case_test:
                    upper_case_test = 1
                continue
            if usr_str[i].islower():  # lower case test
                if not lower_case_test:
                    lower_case_test = 1
                continue

            alpha_numeric_test = 0  # how do I know this

    if length_test and digit_test and upper_case_test and lower_case_test \
            and repeat_test and alpha_numeric_test:
        print("Success! You chose a great password")
        break
    else:
            print("Try another password")
