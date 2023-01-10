n = int(input())
move = list(input().split())
print(move)

move_x = 1
move_y = 1

for step in move:
    if step == 'U' :
        if move_x>1:
            move_x = move_x-1
    
    elif step =='D':
        if move_x<5:
            move_x = move_x+1
            
        
    elif step =='R':
        if move_y<5:
            move_y = move_y+1

        
    elif step =='L':
        if move_y>1:
            move_y = move_y-1
            
print(move_x+' '+move_y)
    