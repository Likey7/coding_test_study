#위상정렬

from collections import deque
import copy
v = int(input())
indegree = [0] * (v+1)
graph = [[] for i in range(v+1)]
time = [0] *(v+1)

for i in range(1,v+1):
    data = list(map(int,input().split()))
    time[i]=data[0]
    for x in data[1:-1]:
        indegree[i]+=1
        graph[x].append(i)

def topology_sort():
    result = copy.deepcopy(time)
    q = deque()
    
    for i in range(1,v+1):
        if indegree[i]==0:
            q.append(i)
            
    while q :
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i],result[now]+time[i])
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)
                
    for i in range(1,v+1):
        print(result[i])
        
topology_sort()


'''

n개의 정수를 한 줄에 출력한다. 출력하는 숫자는 올해 순위이며, 1등팀부터 순서대로 출력한다. 
만약, 확실한 순위를 찾을 수 없다면 "?"를 출력한다. 
데이터에 일관성이 없어서 순위를 정할 수 없는 경우에는 "IMPOSSIBLE"을 출력한다.
'''