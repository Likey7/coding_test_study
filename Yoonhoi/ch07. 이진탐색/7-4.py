# 빠르게 입력받기 
import sys
input_data = sys.stdin.readline().rstrip()

print(input_data)

'''
sys 라이브러리를 사용할 때는 한 줄 입력받고 나서 rstrip() 함수를 꼭 호출해야 한다. 
소스코드에 엔터가 줄바꿈 기호로 입력되는데 
이 공백 문자를 제거하기 위함. 

'''