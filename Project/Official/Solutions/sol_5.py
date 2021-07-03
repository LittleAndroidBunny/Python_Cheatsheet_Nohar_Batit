#### Worksheet #5 ####


### Q1 ###

def a(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return a(n - 1) + a(n - 2) + 2 * a(n - 3)


### Q2 ###

def GCD(x, y):
    if x % y == 0 and x != y:
        return min(x, y)
    elif x == y:
        return x
    elif x % y == 1:
        return 1
    else:
        Min = min(x, y)
        R = max(x, y) / min(x, y)
        return GCD(R, Min)


### Q3 ###

def Q3(a, b):
    if b == 1:
        return a
    else:
        return a * Q3(a, b - 1)


###### Part 2 - Dictionaries #####

### Q4 ###


def Dict_maker(Str):  ### Assumes Str is a string of small words seperated by commas
    word_list = Str.split(",")
    Dict = {'a': [], 'b': [], 'c': [], 'd': [], 'e': [], 'f': [], 'g': [], 'h': [], 'i': [], 'j': [], 'k': [], 'l': [],
            'm': [], 'n': [], 'o': [], 'p': [], 'q': [], 'r': [], 's': [], 't': [], 'u': [], 'v': [], 'w': [], 'x': [],
            'y': [], 'z': []}
    for i in range(len(word_list)):
        letter = word_list[i][0]
        L = Dict[letter]
        L.append(word_list[i])
        Dict[letter] = L
    return Dict


Str = "dad,mom,omer,man,dog,walk"

print(Dict_maker(Str))


### Q5 ###

def First_counter(Dict):
    a2z = "abcdefghijklmnopqrstuvwxyz"
    result = []
    values = list(Dict.values())  ### values is now a list of lists
    for i in range(len(a2z)):
        c = 0
        for n in values[i]:
            if n[0] == a2z[i]:
                c += 1
        result.append((a2z[i], c))


Dict = {'a': [], 'b': [], 'c': [], 'd': [], 'e': [], 'f': ['fwf'], 'g': [], 'h': [], 'i': [], 'j': [], 'k': [], 'l': [],
        'm': [],
        'n': [], 'o': [], 'p': [], 'q': ['qrfqf'], 'r': [], 's': [], 't': [], 'u': [], 'v': [],
        'w': ['wer', 'wrw', 'wf',
              'wfqrf', 'wqfrefre'], 'x': [], 'y': [], 'z': []}

print(First_counter(Dict))











