"""
FAVORITO:

def meeting(s):
    return ''.join(sorted('({1}, {0})'.format(*(x.split(':'))) for x in s.upper().split(';')))


"""



"""
https://www.codewars.com/kata/59df2f8f08c6cec835000012/train/python

John has invited some friends. His list is:

s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill";
Could you make a program that

makes this string uppercase
gives it sorted in alphabetical order by last name.
When the last names are the same, sort them by first name. Last name and first name of a guest come in the result between parentheses separated by a comma.

So the result of function meeting(s) will be:

"(CORWILL, ALFRED)(CORWILL, FRED)(CORWILL, RAPHAEL)(CORWILL, WILFRED)(TORNBULL, BARNEY)(TORNBULL, BETTY)(TORNBULL, BJON)"
It can happen that in two distinct families with the same family name two people have the same first name too.

Notes
You can see another examples in the "Sample tests".
"""

def meeting(s):
    s= s.upper()
    
    dictionary = {}
    
    for element in s.split(";"):
        name,lastName= element.split(":")[0], element.split(":")[1]
        
        if lastName in dictionary.keys():
            dictionary[lastName].append(name)
        else:
            dictionary.setdefault(lastName, [name])
    
    sortedList= sorted( dictionary.items() )
    
    for element in sortedList:
        if len(element[1])>1:
            element[1].sort()
    
    stringOfNames=""
    
    
    print("\n"*2)
    
    
    for element in sortedList:
        if len(element[1])> 1:
            for names in element[1]:
                stringOfNames += "({}, {})".format(element[0],names)
        else:
            stringOfNames += "({}, {})".format(element[0],element[1][0])
    
    return stringOfNames
            
                


print(meeting("Alexis:Wahl;John:Bell;Victoria:Schwarz;Abba:Dorny;Grace:Meta;Ann:Arno;Madison:STAN;Alex:Cornwell;Lewis:Kern;Megan:Stan;Alex:Korn"))

#"(ARNO, ANN)(BELL, JOHN)(CORNWELL, ALEX)(DORNY, ABBA)(KERN, LEWIS)(KORN, ALEX)(META, GRACE)(SCHWARZ, VICTORIA)(STAN, MADISON)(STAN, MEGAN)(WAHL, ALEXIS)"