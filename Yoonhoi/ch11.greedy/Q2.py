S = list(map(int,list(input())))

SUM = S[0]

for i,x in enumerate(S[1:]):
    print(x)
    if SUM==0 :
        SUM +=x
    elif x ==0 or x==1:
        SUM +=x
    else : 
        SUM*=x
        
print(SUM)

