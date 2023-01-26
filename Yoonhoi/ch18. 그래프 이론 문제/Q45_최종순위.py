# https://www.acmicpc.net/problem/3665
'''
첫째 줄에는 테스트 케이스의 개수가 주어진다. 테스트 케이스는 100개를 넘지 않는다. 각 테스트 케이스는 다음과 같이 이루어져 있다.

팀의 수 n을 포함하고 있는 한 줄. (2 ≤ n ≤ 500)
n개의 정수 ti를 포함하고 있는 한 줄. (1 ≤ ti ≤ n) ti는 작년에 i등을 한 팀의 번호이다. 1등이 가장 성적이 높은 팀이다. 
모든 ti는 서로 다르다.
상대적인 등수가 바뀐 쌍의 수 m (0 ≤ m ≤ 25000)
두 정수 ai와 bi를 포함하고 있는 m줄. (1 ≤ ai < bi ≤ n) 상대적인 등수가 바뀐 두 팀이 주어진다. 
같은 쌍이 여러 번 발표되는 경우는 없다.

'''
from collections import deque
import sys

input = sys.stdin.readline


def topology_sort():
    result =0
    q = deque()
    
    for i in range(1,n+1):
        if indegree[i]==0:
            q.append(i)
            
    while q : 
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -=1
            if indegree[i]==0:
                q.append(i)
    
    for i in result:
        print(i,end = ' ')


for _ in range(int(input())):
    n = int(input()) # 전체 팀 개수 
    tis = list(map(int,input().split()))
    # 기존 그래프 그리기 
    
    next = [i for i in range(n)]
    for i in range(len(tis)-1):
        next[tis[i]] = tis[i+1]
        
    
    m = int(input())
    for _ in range(m):
        ai, bi = map(int,input().split())
        # ai-> bi 
        '''
        
    indegree = [0] *(n+1)
    graph = [[] for i in range(n+1)]
    m = int(input())
    for _ in range(m):
        ai, bi = map(int,input().split())
        graph[ai].append(bi)
        indegree[bi]+=1
        '''
    topology_sort()
    
    
    '''
n개의 정수를 한 줄에 출력한다. 출력하는 숫자는 올해 순위이며, 1등팀부터 순서대로 출력한다. 
만약, 확실한 순위를 찾을 수 없다면 "?"를 출력한다. 
데이터에 일관성이 없어서 순위를 정할 수 없는 경우에는 "IMPOSSIBLE"을 출력한다.'''