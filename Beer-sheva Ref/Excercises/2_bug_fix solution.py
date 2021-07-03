# correct way
def code_letters(str1, coding_dict, idx):
    """

    :param str1: The encoded string
    :param coding_dict: the coding dictionary
    :param letter: the current letter to be encoded
    :return: the updated string
    """
    str2 = str1[0:idx] + str1[idx:].replace(str1[idx], coding_dict[str1[idx]], 1)
    return str2     # need to return the new string


def abra(str1, dict1):
    """
    Recive a string and a coding dictionary and encode the string
    :param str1: the target string
    :param dict1: the coding dictionary
    :return: the encoded string
    """
    for i in range(len(str1)):
        str1 = code_letters(str1, dict1, i)     # need to save the new string after the change
    return str1


def kadabra(code):
    """
    Recive the number 'code' and create a dictionary of a cyclic coding with distance 'code' between letters
    :param code: an integer for the cyclic rotation
    :return: a dictionary that represents the coded letter for each letter between 'a'-'z'
    """
    t = {chr(i): chr(i + code) for i in range(ord('a'), ord('z') + 1)}
    t.update({chr(ord('z') - i): chr(code - i - 1 + ord('a')) for i in range(code)})
    return t



circular_coding = 5

coding_dict = kadabra(circular_coding)

print(abra("abrakadabra", coding_dict))


# def foo1(str1):
#     h1 = {}
#     for c in str1:
#          h1[c] = h1.get(c,0) + 1    # remove ,0 from get
#     # h1['str'] = str1
#     return h1
