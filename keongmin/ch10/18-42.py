G = int(input())
P = int(input())

g_ = []
for _ in range(P):
    g_ .append(int(input()))

docking = [False for i in range(G)]
docking[0] = True
