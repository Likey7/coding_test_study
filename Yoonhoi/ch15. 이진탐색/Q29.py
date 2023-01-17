# 공유기 설치 
import sys
f = sys.stdin.readline
n,m = map(int,input().split())
house = []
for i in range(n):
    house.append(int(f().rstrip()))

print(house)