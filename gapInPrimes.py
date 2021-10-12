
"""
The prime numbers are not regularly spaced. For example from 2 to 3 the gap is 1. From 3 to 5 the gap is 2. From 7 to 11 it is 4. Between 2 and 50 we have the following pairs of 2-gaps primes: 3-5, 5-7, 11-13, 17-19, 29-31, 41-43

A prime gap of length n is a run of n-1 consecutive composite numbers between two successive primes (see: http://mathworld.wolfram.com/PrimeGaps.html).

We will write a function gap with parameters:

    g (integer >= 2) which indicates the gap we are looking for

    m (integer > 2) which gives the start of the search (m inclusive)

    n (integer >= m) which gives the end of the search (n inclusive)

    n won't go beyond 1100000.

In the example above gap(2, 3, 50) will return [3, 5] or (3, 5) or {3, 5} which is the first pair between 3 and 50 with a 2-gap.

So this function should return the first pair of two prime numbers spaced with a gap of g between the limits m, n if these numbers exist otherwise `nil or null or None or Nothing (or ... depending on the language).

In C++, Lua: return in such a case {0, 0}. In F#: return [||]. In Kotlin, Dart and Prolog: return []. In Pascal: return Type TGap (0, 0).
Examples:

    gap(2, 5, 7) --> [5, 7] or (5, 7) or {5, 7}

    gap(2, 5, 5) --> nil. In C++ {0, 0}. In F# [||]. In Kotlin, Dart and Prolog return []`

    gap(4, 130, 200) --> [163, 167] or (163, 167) or {163, 167}

([193, 197] is also such a 4-gap primes between 130 and 200 but it's not the first pair)

    gap(6,100,110) --> nil or {0, 0} or ... : between 100 and 110 we have 101, 103, 107, 109 but 101-107is not a 6-gap because there is 103in between and 103-109is not a 6-gap because there is 107in between.

    You can see more examples of return in Sample Tests.
"""
#from sympy import isPrime

if __name__ == "__main__":
   

    """

    def listOfPrime(start,end):
        return [idx for idx in range(start,end+1) if isPrime(idx)]

    

    print("is prime: ",listOfPrime(1,50))

    def gap(g, m, n):
        listPrimeNumbers= listOfPrime(m,n)

        for idx in range(0,len(listPrimeNumbers)-1):
            if listPrimeNumbers[idx+1] - listPrimeNumbers[idx] == g:
                return [listPrimeNumbers[idx],listPrimeNumbers[idx+1]]

        return None

    """


    """
    def gap(g,m,n):
        listPrimeNumbers=[]
        for idx in range(m,n+1):
            if isPrime(idx):
            #if sympy.isPrime(idx):
                listPrimeNumbers.append(idx)

                try:
                    #print(listPrimeNumbers[len(listPrimeNumbers)-1], "-", listPrimeNumbers[len(listPrimeNumbers)-2],"=",listPrimeNumbers[len(listPrimeNumbers)-1]- listPrimeNumbers[len(listPrimeNumbers)-2])
                    if (listPrimeNumbers[len(listPrimeNumbers)-1]- listPrimeNumbers[len(listPrimeNumbers)-2])== g:
                        #print("ENTRA EN EL IF")

                        return [listPrimeNumbers[len(listPrimeNumbers)-2],listPrimeNumbers[len(listPrimeNumbers)-1]]
                except :
                    pass
        return None
    """
    def isPrime(number):
        if number %2==0:
            return False
        for idx in range(3,number//2+1,2):
            if number %idx ==0:
                return False
        
        return True

    def gap(g,m,p):

        if isPrime(g):
            return None
        numberSave= None
        if m%2 ==0:
            m +=1        

        for idx in range(m,p+1,2):
            if isPrime(idx):
                    
                if numberSave and idx-numberSave==g:
                    return [numberSave,idx]
                
                numberSave= idx
            
        return None
                
                            
                        

    def listOfPrime(start,end):
        return [idx for idx in range(start,end+1) if isPrime(idx)]

    print(listOfPrime(1,50))

    print("gap (2,100,150): ",gap(2,100,150))

    print("gap (2,100,150): ",gap(10,300,400))

    print("gap(7,3,1100000): ",gap(7,3,1100000))

    print("gap(546,3,1100000): ",gap(546,3,1100000))

    