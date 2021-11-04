"""

Link= https://www.codewars.com/kata/54f8693ea58bce689100065f/train/python

Given a rational number n

n >= 0, with denominator strictly positive

    as a string (example: "2/3" in Ruby, Python, Clojure, JS, CS, Go)
    or as two strings (example: "2" "3" in Haskell, Java, CSharp, C++, Swift, Dart)
    or as a rational or decimal number (example: 3/4, 0.67 in R)
    or two integers (Fortran)

decompose this number as a sum of rationals with numerators equal to one and without repetitions (2/3 = 1/2 + 1/6 is correct but not 2/3 = 1/3 + 1/3, 1/3 is repeated).

The algorithm must be "greedy", so at each stage the new rational obtained in the decomposition must have a denominator as small as possible. In this manner the sum of a few fractions in the decomposition gives a rather good approximation of the rational to decompose.

2/3 = 1/3 + 1/3 doesn't fit because of the repetition but also because the first 1/3 has a denominator bigger than the one in 1/2 in the decomposition 2/3 = 1/2 + 1/6.
Example:

(You can see other examples in "Sample Tests:")

decompose("21/23") or "21" "23" or 21/23 should return 

["1/2", "1/3", "1/13", "1/359", "1/644046"] in Ruby, Python, Clojure, JS, CS, Haskell, Go

"[1/2, 1/3, 1/13, 1/359, 1/644046]" in Java, CSharp, C++, Dart

"1/2,1/3,1/13,1/359,1/644046" in C, Swift, R

Notes

    The decomposition of 21/23 as

    21/23 = 1/2 + 1/3 + 1/13 + 1/598 + 1/897

    is exact but don't fulfill our requirement because 598 is bigger than 359. Same for

    21/23 = 1/2 + 1/3 + 1/23 + 1/46 + 1/69 (23 is bigger than 13)
    or 
    21/23 = 1/2 + 1/3 + 1/15 + 1/110 + 1/253 (15 is bigger than 13).

    The rational given to decompose could be greater than one or equal to one, in which case the first "fraction" will be an integer (with an implicit denominator of 1).

    If the numerator parses to zero the function "decompose" returns [] (or "",, or "[]").

    The number could also be a decimal which can be expressed as a rational.

Example:

0.6 in Ruby, Python, Clojure,JS, CS, Julia, Go

"66" "100" in Haskell, Java, CSharp, C++, C, Swift, Scala, Kotlin, Dart, ...

0.67 in R.

Ref: http://en.wikipedia.org/wiki/Egyptian_fraction

Ref: https://en.wikipedia.org/wiki/Greedy_algorithm_for_Egyptian_fractions


"""

from fractions import Fraction

def recursiveDecompose(List,numberCheck):

    try:
        x,y= numberCheck.split("/")
        x=int(x)
        y=int(y)
    except:
        List.append(numberCheck)
        return List
    
    try:
        if x % y ==0 and x> y:
            number= "{}".format(x//y)
            List.append(number)
            return List
        elif y % x == 0:
            number= "1/{}".format((y//x))
        else:
            number= "1/{}".format((y//x +1))

        """
        if y % x== 0:
            List.append("1/{}".format( y//x ) )
        else:
            List.append("1/{}".format( y//x +1 ) )
        """
    except:
        return
    
    i,j= number.split("/")
    if i==j:
        List.append("1")
    else:
        List.append(number)

    recursiveDecompose(List, ( "{}/{}".format((-y) % x , y*(y//x +1)) ))

def decompose(n):    

    try:
        n= str(Fraction(n))
    except:
        pass
    if n=="0":
        return []
    List= []
    recursiveDecompose(List,n)
    return List

u= decompose('1.25')
print(u)

u= decompose('1')
print(u)


u= decompose('0.66') #['1/2', '1/7', '1/59', '1/5163', '1/53307975']

print(u)
u= decompose('4/5') #["1/2", "1/4", "1/20"]

print(u)

u= decompose('75/3') #["25"]

print(u)

