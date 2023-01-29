# A를 편집하여 문자열 B를 만든다.
# 삽입, 삭제, 교체
# 편집 거리란 문자열 A를 편집하여 B로 만들기 위한 연산의 수

A = input()
B = input()

n = len(A)
m = len(B)

# 초기화

dp = [[0] * (n+1) for _ in range(m+1)]

# if len(A) > len(B): # 개수가 A가 많으면 삭제
#     A[]        
# elif len(A) < len(B): # 개수가 B가 많으면 삽입


for i in range(1, n+1):
    for j in range(1, m+1):

        
        # 개수가 같으면 교체
        if A[i] != B[j]:
            d[j] = A[i]



#         if i != j:

#         # 삽입

#         # 삭제

#         # 변경
#         if e:
#             e
# 글자수 체크
# result = abs(len(A) - len(B))

# print(result)
