
# stack 을 사용
def recursive_function(i)  :
     print('재귀 함수를 호출합니다. ')
     if i==10:
         return
     recursive_function(i+1)
     
     
recursive_function(1)