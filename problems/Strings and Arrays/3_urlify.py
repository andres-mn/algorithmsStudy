def urlify(string):
    algo = '''

    str = "Mr John Smith    "
    -->   "Mr%20John%20Smith"

    str = "Mr John Smith    "
           i
                      
    str = "Mr%20John%20Smith"   

'''
    
    i = len(string)-1

    while string[i] == ' ':
        i = i-1

    #finding first non whitespace char
    #move char to rightmost
    while i >= 0:
        
        if string[i] == ' ':
            j=i
            while j+1< len(string) and string[j+1] == ' ':
                j = j+1
            string[j] = '0'
            string[j-1] = '2'
            string[j-2] = '%'
            i = i-1
            continue

        if string[i] != ' ':
            j = i
            while j+1< len(string) and string[j+1] == ' ':
                j = j+1
            if string[j] != ' ':
                i = i-1
                continue
            string[j] = string[i]
            #moving char to end
            #making moved character = whitespace
            string[i] = ' '
            i = i-1
    
    print("".join(string))
    

if __name__ == "__main__":
    string = list("Mr John Smith    ")
    print("".join(string))

    urlify(string)
