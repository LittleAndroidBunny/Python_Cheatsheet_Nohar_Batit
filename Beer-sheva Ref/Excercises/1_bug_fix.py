def code_letters(str1, coding_dict, letter):
    str1.replace(letter, coding_dict[letter])


def abra(str1, dict1):
    for i in range(len(str1)):
        code_letters(str1, dict1, str1[i])
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
