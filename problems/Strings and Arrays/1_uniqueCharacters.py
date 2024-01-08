def solve(str):
    explanation = '''

        string = abca
                    i

                 
        set = {a,b,c}
        return False

         string = abc
                    i

                 
        set = {a,b,c}
        return True
'''
    set1 = set()
    for character in str:
        if character in set1:
            return False
        else:
            set1.add(character)
    return True
        


if __name__ == "__main__":
    str = "abcdeft"
    print(solve(str))

    timeComp = '''
    O(N) where N is len(str1)
'''