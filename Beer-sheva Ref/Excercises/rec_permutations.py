

def rec_permutation(data, perm_length):
    """
    This function is a recursive implementation of choosing "k" elements
    out of "n" options with returning occurrences
    :param data: the "n" length data base
    :param perm_length: the number of elements to choose "k"
    :return: res_list: a list of lists of all possible permutations
    """
    if perm_length == 1:
        return [[atom] for atom in data]

    res_list = []                   # how can we make it better ?
    smaller_perm = rec_permutation(data, perm_length-1)
    for elem in data:
        for sub_combination in smaller_perm:
            res_list.append([elem] + sub_combination)
    return res_list


print(rec_permutation([1, 2, 3], 3))
