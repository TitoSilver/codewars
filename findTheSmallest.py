"""

Link: https://www.codewars.com/kata/573992c724fc289553000e95/train/python


You have a positive number n consisting of digits. You can do at most one operation: Choosing the index of a digit in the number, remove this digit at that index and insert it back to another or at the same place in the number in order to find the smallest number you can get.
Task:

Return an array or a tuple or a string depending on the language (see "Sample Tests") with

        the smallest number you got
        the index i of the digit d you took, i as small as possible
        the index j (as small as possible) where you insert this digit d to have the smallest number.

Examples:

smallest(261235) --> [126235, 2, 0] or (126235, 2, 0) or "126235, 2, 0"

126235 is the smallest number gotten by taking 1 at index 2 and putting it at index 0

smallest(209917) --> [29917, 0, 1] or ...

[29917, 1, 0] could be a solution too but index `i` in [29917, 1, 0] is greater than 
index `i` in [29917, 0, 1].

29917 is the smallest number gotten by taking 2 at index 0 and putting it at index 1 which gave 029917 which is the number 29917.

smallest(1000000) --> [1, 0, 6] or ...

Note

Have a look at "Sample Tests" to see the input and output in each language


"""
def checkSmall(l,idx):

    # print("idx: {}".format(idx))

    minValue= ord(l[idx])
    minIdx= 0

    for i in range(idx,len(l)):
        if ord(l[i])<= minValue:
            minValue= ord(l[i])
            minIdx= i
    
    return minIdx

def replace(l,newIdx,idx):
    # print("newIdx: {}; idx: {}".format(newIdx,idx))

    t=l.copy()
    t.insert(idx,t.pop(newIdx))
    return t


def smallest(n):

    stringN= str(n)
    l=[ x for x in stringN ]

    for idx in range(0,len(l)):
        
        newIdx= checkSmall(l,idx)
        
        t= replace(l,newIdx,idx)

        # print("l: {}\nt: {}\nt!=l: {}".format(l,t,t!=l))

        if t!= l:
            return [int("".join((x for x in t))),newIdx,idx]






print("smallest: ",smallest(261235)) # [126235, 2, 0])
print("smallest: ",smallest(209917)) # [29917, 0, 1])
print("smallest: ",smallest(285365)) # [238565, 3, 1])
print("smallest: ",smallest(269045)) # [26945, 3, 0])
print("smallest: ",smallest(296837)) # [239687, 4, 1])
