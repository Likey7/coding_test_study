# 여행 계획에 해당하는 모든 노드가 같은 집합에 속하기만 하면 여행 가능한 경로라는 것이다. 
# 두 노드 사이에 도로가 존재하면 ㅎ바집합연산을 이용해, 같은 집합으로넣는다. 
# 결과적으로, 여행 계획에 해당하는 모든 노드가 모두 같은 집합에 속하는지를 체크해서 출력한다. 
# 서로소 집합으로 해결할 수 있는 문제 
def find_parent(parent,x):
    if parent[x]!=x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] =b
        
n,m  = map(int,input().split())
parent = [i for i in range(n+1)]

for i in range(n):
    data = list(map(int,input().split()))
    for j in range(n):
        if data[j] ==1 : 
            union_parent(parent,i+1,j+1)
            
plan = list(map(int,input().split()))

result = True
for i in range(m-1):
    if find_parent(parent,plan[i]) != find_parent(parent,plan[i+1]):
        result = False

if result : 
    print('YES')
else:
    print('NO')