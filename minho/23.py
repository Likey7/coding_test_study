# 1. 국어 점수가 감소하는 순서로
# 2. 국어 점수가 같으면 영어 점수가 증가하는 순서로
# 3. 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
# 4. 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로 (아스키코드는 대문자는 소문자보다 작음)
# 이름, 국어, 영어, 수학
N = int(input())

array = []

for i in range(N):
    name, h, e, m = input().split()
    array.append([name, int(h), int(e), int(m)])

# 조건 역순
array.sort(key = lambda x: x[0])
array.sort(key = lambda x: x[3], reverse=True)
array.sort(key = lambda x: x[2])
array.sort(key = lambda x: x[1], reverse=True)

for i in array:
    print(i[0])