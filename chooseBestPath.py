"""
https://www.codewars.com/kata/55e7280b40e1c4a06d0000aa/train/python
"""

"""
--BEST PRACTICE--
import itertools
def choose_best_sum(t, k, ls):
    try: 
        return max(sum(i) for i in itertools.combinations(ls,k) if sum(i)<=t)
    except:
        return None

"""

def findSolution(t,k,checkList):
    """
    compara si la cantidad de destinos posibles es igual a la cantidad de destinos k
    compara si la distancia de los destinos posibles es igual o menor a la cantidad de destinos t
    """
    if len(checkList)==k and sum(checkList)<= t:
        return True
    return False

    
def recursiveBestSum(t,k,ls,checkList,solutionFound):
    
    if findSolution(t,k,checkList):
        return sum(checkList)
    
    for idx in range(0,len(ls)):
        
        checkList.append(ls[idx])
        verifyList= recursiveBestSum(t,k,ls[idx+1:],checkList,solutionFound)
        if verifyList:
            solutionFound.append(verifyList)
        
        checkList.pop()
def choose_best_sum(t, k, ls):
    print("t: {}, k: {}".format(t,k))
    
    ls.sort(reverse=True) 
    print(ls)
    checkList=[]
    solutionFound=[]
    recursiveBestSum(t,k,ls[:],checkList,solutionFound)
    setDistance= set(solutionFound)
    print(setDistance)

    if setDistance:
        return max(setDistance)
    else:
        return None
    
xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
t1= choose_best_sum(230, 4, xs)
#t2= choose_best_sum(430, 5, xs)
#t3= choose_best_sum(430, 8, xs)

print("t1: {}".format(t1))