N = int(input())

for x in range(N+1):
    for j in range(60):
        for i in range(60) :
            if '3' in str(x) + str(j)+str(i) :
                count +=1
print(count)