
"""
    FAVORITO:

    def cut_log(p, n):
    log = [0]
    for _ in range(n):
        log.append(max(pi + li for pi, li in zip(p[1:], log[::-1])))
    return log[n]

"""


"""

https://www.codewars.com/kata/54b058ce56f22dc6fe0011df/train/python

CLEAR CUTTER'S NEEDS YOUR HELP!
The logging company Clear Cutter's makes its money by optimizing the price-to-length of each log they cut before selling them. An example of one of their price tables is included:

# So a price table p
p = [ 0,  1,  5,  8,  9, 10]

# Can be imagined as:
# length i | 0  1  2  3  4  5 *in feet*
# price pi | 0  1  5  8  9 10 *in money*
They hired an intern last summer to create a recursive function for them to easily calculate the most profitable price for a log of length n using price table p as follows:

def cut_log(p, n):
    if (n == 0):
        return 0
    q = -1
    for i in range(1, n+1)
        q = max(q, p[i] + cut_log(p, n-i))
    return q
An example of the working code:

cut_log(p, 5) # => 13
# 5ft = $10, BUT 2ft + 3ft = 5ft -> $5 + $8 = $13 which is greater in value
However, their senior software engineer realized that the number of recursive calls in the function gives it an awful running time of 2^n (as this function iterates through ALL 2^n-1 possibilities for a log of length n).

Having discovered this problem just as you've arrived for your internship, he responsibly delegates the issue to you.

Using the power of Stack Overflow and Google, he wants you to create a solution that runs in Θ(n^2) time so that it doesn't take 5 hours to calculate the optimal price for a log of size 50. (He also suggests to research the problem using the keywords in the tags)

(Be aware that if your algorithm is not efficient, it will attempt to look at 2^49 = 562949953421312 nodes instead of 49^2 = 2401... The solution will automatically fail if it takes longer than 6 seconds... which occurs at right around Log 23)

"""
def proffit(checkTable,maxProffit):

    
    #calcula el mayor valor que puede obtener 

    if len(maxProffit)==0:
        return checkTable[0]

    lenIterator= len(checkTable)


    calculeteProffit= checkTable[len(checkTable)-1]

    if lenIterator %2 ==0:
        #even
        for idx in range(1,len(checkTable)//2):
            calculeteProffit= max(calculeteProffit, maxProffit[idx] + maxProffit[lenIterator-1 -idx] )
    
    else:
        #odd
        for idx in range(1, len(checkTable)//2 +1):
            calculeteProffit= max(calculeteProffit, maxProffit[idx] + maxProffit[lenIterator-1 -idx] )


    return calculeteProffit

            

def cut_log(p, n):

    maxProffit=[]

    for idx in range(1,n+2):
        maxProffit.append( proffit( p[:idx],maxProffit ) )

    
    
    return  maxProffit[len(maxProffit)-1]

"""
p = [  0,   1,   5,   8,   9,  10,  17,  17,  20,  24, # 0X's
      30,  32,  35,  39,  43,  43,  45,  49,  50,  54, # 1X's
      57,  60,  65,  68,  70,  74,  80,  81,  84,  85, # 2X's
      87,  91,  95,  99, 101, 104, 107, 112, 115, 116, # 3X's
     119] # 40th element

"""

p = [  0,   1,   5,   8,   9,  10,  17,  17,  20,  24, 30,  32,  35,  39,  43,  43,  45,  49,  50,  54,57,  60,  65,  68,  70,  74,  80,  81,  84,  85, 87,  91,  95,  99, 101, 104, 107, 112, 115, 116, 119] # 40th element

#print("p: ",list(enumerate(p)))



cut_log(p, 5)# 13

cut_log(p, 8)# 22