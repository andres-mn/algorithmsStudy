
def convertStringToDictionary(someString):
    explanation = '''

        string = abca
                     i

        dict = {a:2, b:1, c:1, }

'''
    dictionary = {}

    for mycharacter in someString: 
        if mycharacter in dictionary.keys():
            dictionary[mycharacter] += 1

        else:
            dictionary[mycharacter] = 1


    return dictionary


def decidePermutations(str1, str2):
    # Decides if str2 is a permutation of str1 or vice versa

    #pseudocode and examples

    examples = '''

    str1 = abc
    str2 = bca
    str1 is a permutation of str2 --> True
 -------
    str1 = abd
    str2 = bca
    str1 is NOT a permutation of str2 --> False

    1st thing to check: length must be equal

    str1 = abc -> {a:1, b:1, c:1}
    str2 = bca -> {b:1, c:1, a:1}
    --> TRUE

    str1 = aabc -> {a:2, b:1, c:1}
    str2 = bdaa -> {b:1, d:1, a:2}
    --> FALSE

'''

    if len(str1) != len(str2):
        return False
    
    dictionary1 = convertStringToDictionary(str1)
    dictionary2 = convertStringToDictionary(str2)

    checkIfEqual = dictionary1 == dictionary2

    return checkIfEqual
    

if __name__ == "__main__":
    str1 = "abc"
    str2 = "bac"

    print(decidePermutations(str1, str2))

    timeComp = '''
    O(N) where N is len(str1)
'''