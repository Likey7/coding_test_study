import itertools
from collections import deque
import copy

lab =  [[2, 0, 0, 0, 1, 1, 0],
        [0, 0, 1, 0, 1, 2, 0],
        [0, 1, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0]]



def makewall(count):
    for i in range(n):
        for j in range(m):

            if count == 3:
                bfs()
                return 


            if lab[i][j] == 0:
                lab[i][j] = 1
                makewall(count+1)

def bfs():
    queue = deque()
    tmp = copy.deepcopy(lab)
    

