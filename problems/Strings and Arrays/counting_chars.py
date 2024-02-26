def count_characters(string):

    # iterate over the string character by character

    # counts is a dictionary { key : value }
    counts = {}
    
    # string = "aabbcc"
    #            i
    #

    for character in string:
        if character not in counts.keys():
            counts[character] = 1
            # { 'a' : 1 }
            # counts['a'] // equal to 1
        
        else:
            counts[character] +=1
            # { 'a' : 2 }
            # counts['a'] // equal to 2

    print(counts)



if __name__ =="__main__":
    # a function to count characters in a string
    # the count for each character
    # for example: 
    # string = "aabbcc"
    #  counts = {
    #   a : 2,
    #   b : 2,
    #   c : 2
    #   }
    string = "aabbcc"
    count_characters(string)

    problem = '''

        Given a string, what's the length of longest palindrome
        string that we can form using its characters?

        palindromes: aba abcdcba

        string = "abbd"
        //longest palindrome here is "bab" or "bdb"
        length_of_longest_palindrome(string) = 3

        counts = {
              a : 1,
              b : 2,
              d : 1 
              }
            bab


        string = "122312"
        // longest palindrom is = "12221"

        counts = {
            '1' : 2,
            '2' : 3,
            '3' : 1
        }
        12221

        string = "1112231277777"

        count = {
            '1' : 4
            '2' : 3
            '3' : 1
            '7' : 5
        }
        117777711
        odd numbers
        even numbers 
        

        string = "abab"
        // longest palindrome = "abba"



'''