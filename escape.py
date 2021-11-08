"""
You're stuck in a maze and have to escape. However, the maze is blocked by various doors and you'll need the correct key to get through a door.
Basic instructions

You are given a grid as the input and you have to return the positions to go through to escape.

To escape, you have to collect every key and then reach the exit (the exit can only be unlocked if you have every key).

There are also doors in the way, and you can only get through a door if you have the corresponding key.
More detail

The grid is given as a tuple of string representing rows of a grid. The start position is given by '@' and the end position is given by '$'. Walls are given by '#'

Doors are represented by an upper case letter eg. 'A'. And the corresponding key is represented by the lower case letter. For example. the key 'b' unlocks the door 'B'. To collect a key, you just have to travel over the position where it is located (it is automatically picked up).

You can move in 4 directions: up, down, left or right. You cannot move diagonally. You also cannot move out of the grid or through walls.

To escape, you have to return the shortest path to travel through to reach the end. You have to return a list of all the positions you travel through (including the start and end) in the cartesian form (x, y), with x being the horizontal position, and y being vertical position. (0, 0) will be the top left position. The shortest path is defined by the least amount of moves you have to make. If there is no solution, you should return None.

You will have to deal with up to 8 keys per grid. There will always be as many keys as doors, and you have to collect all the keys to be able to escape through the exit. You can only travel through doors if you have the correct key. However, you can travel over the exit even if you don't have all the keys (imagine that the exit is a trapdoor).

You do not need collect the keys in alphabetical order.

For example:

grid2 in the sample tests is:
(
  '.a..',
  '##@#',
  '$A.#'
)
You should return:
[(2, 1), (2, 0), (1, 0), (2, 0), (2, 1), (2, 2), (1, 2), (0, 2)]
as you have to go upwards to get key `a` before being able to go though door `A` to get to the exit.

grid3 in the sample tests is:
(
  'aB..',
  '##@#',
  '$Ab#'
)
You should return:
[(2, 1), (2, 2), (2, 1), (2, 0), (1, 0), (0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (1, 2), (0, 2)]

If no keys are given, then you just have to reach the exit. If there are multiple shortest solutions, you can return any of them.

There are 101 tests in total: 8 sample tests and 93 random tests. The largest random tests will have maximum side lengths of 50 x 50

"""

class Grid:

    keys={}
    doors={}
    empyPath=[]
    initGame=None
    exitGame=None
    path= []

    def __init__(self, grid):

        for idxElement in range(0,len(grid)):
            for idxSquere in range(0,len(grid[idxElement])):
                if grid[idxElement][idxSquere].islower():
                    self.keys.setdefault(grid[idxSquere][idxSquere], (idxElement,idxSquere))
                    self.path.append((idxElement,idxSquere))

                elif grid[idxElement][idxSquere].isupper():
                    self.doors.setdefault(grid[idxElement][idxSquere], (idxElement,idxSquere))
                    self.path.append((idxElement,idxSquere))

                elif grid[idxElement][idxSquere]==".":
                    self.empyPath.append((idxElement,idxSquere))
                    self.path.append((idxElement,idxSquere))

                elif grid[idxElement][idxSquere]== "@":
                    self.initGame= (idxElement,idxSquere)
                    self.path.append((idxElement,idxSquere))

                elif grid[idxElement][idxSquere]=="$":
                    self.exitGame=(idxElement,idxSquere)
                    self.path.append((idxElement,idxSquere))
class Graph:
    matrix=[]
    DictDependencies= None

    def __init__(self,path):            
        for x in path:
            row=[]
            for y in path:
                if x[0]-1 <= y[0] <= x[0]+1:
                    if x[1] -1 <= y[1] <= x[1] +1:
                        if (x[0]==y[0] and x[1]!= y[1]) or (x[0]!= y[0] and x[1]== y[1]):
                            row.append(1)
                        else:
                            row.append(0)
                    else:
                        row.append((0))
                else:
                    row.append(0)
            self.matrix.append(row)
        
        self.DictDependencies= dict(map(lambda x: (x[1],x[0]), (x for x in enumerate(path))))



def BFS (grid,graph,root,findX):
    print("root: {}\nfindX: {}".format(root,findX))
    checkNodes= grid.copy()

    conectionNodes=[root]
    count= 0
    while (checkNodes is checkNodes):
        try:
            root= conectionNodes[count]
            checkNodes.remove(root)
        except:
            break

        #insert element in conectionNodes for make a path a tree
        for x in range(0,len(graph.matrix[graph.DictDependencies.get(root)])):
            if graph.matrix[graph.DictDependencies.get(root)][x]==1 and grid[x] not in conectionNodes:
                conectionNodes.append(grid[x])
                if grid[x]== findX:
                    checkNodes=[]
                    break
        
        count += 1

    #make a sieve to eliminate any node that does not correspond to the path between root and final node 

    check= conectionNodes[len(conectionNodes)-1]
    for idx in range( len(conectionNodes)-2,-1,-1):
        if (graph.matrix[graph.DictDependencies.get(check)][graph.DictDependencies.get(conectionNodes[idx])]!= 0):
            check= conectionNodes[idx]
        else:
            conectionNodes.pop(idx)
    
    print(conectionNodes)

def createGraph(grid):

    print("path: ",grid.path)

    graph= Graph(grid.path)

    for element in graph.matrix:
        print(element)
    
    # print("DictDependencies: ",graph.DictDependencies)
    # print("graph.DictDependencies.get((2,1)): ",graph.DictDependencies.get((2,1)))

    BFS(grid.path,graph,(1,2),(2,0))
                            



def solutionEscape(grid):
    for i in grid:
        print(i)
    newGrid=Grid(grid)

    createGraph(newGrid)


table= ('aB..','##@#','$Ab#')
solutionEscape(table)