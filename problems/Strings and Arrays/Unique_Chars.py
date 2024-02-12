def getUniqueChars(string):
    description = '''
        prints unique characters of a string.

        example:

        string = "aabbcd"
        getUniqueCharacters(string) --> "abcd"

    '''
    setsCharacteric = '''

        mySet.add('a')
        mySet.add('a')
        mySet.add('b')

        mySet = {'a','b'}

    '''
    
    mySet = set()
    count = len(string)
    for i in range(len(string)):
        #i = 0 --> len(string)-1
        #for(int i = 0 ; i<string.length ; i++)
        mySet.add(string[i])
        count += 1

    x = 0
    for element in mySet:
        print(element)
        x+=1
    print(x)
    #len(mySeth)

def countCharacters(string):
    #counts characters in a string
    #example: string = "abcde" count = 5
    
    #way 1: obtain length of string
    count = len(string)
    print(count)

    #way 2: iterate through the string
    count = 0

    for i in range(len(string)):
        #i = 0 --> len(string)-1
        #for(int i = 0 ; i<string.length ; i++)
        count += 1

    print(count)

    #Time complexity of both = O(N) where N = len(string)


if __name__ =="__main__":
    sampleString = "aabbcd"
    getUniqueChars(sampleString)