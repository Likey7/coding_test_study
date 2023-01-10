s = list(map(int,list(input())))
left = sum(s[:int(len(s)/2)])
right = sum(s[int(len(s)/2):])
if left==right:
    print('LUCKY')
else:
    print('READY')
    