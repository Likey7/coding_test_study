t = int(input())

def test_case():
  n, m = map(int, input().split())
  gold = list(map(int, input().split()))
  d = [gold[m*i : m*(i+1)] for i in range(n)]

  for i in range(1, m):
    for j in range(n):
      #맨위케이스 ==> 이전인덱스의 왼쪽, 왼쪽아래밖에 안됨
      if j==0:
        left = d[j][i] + d[j][i-1]
        left_down = d[j][i] + d[j+1][i-1]
        d[j][i] = max(d[j][i], left, left_down)
      #맨아래케이스 ==> 이전인덱스의 왼쪽, 왼쪽위밖에 안됨
      elif j==n-1:
        left = d[j][i] + d[j][i-1]
        left_up = d[j][i] + d[j-1][i-1]
        d[j][i] = max(d[j][i], left, left_up)
      #중간케이스 ==> 다됨
      else:
        left = d[j][i] + d[j][i-1]
        left_down = d[j][i] + d[j+1][i-1]
        left_up = d[j][i] + d[j-1][i-1]
        d[j][i] = max(d[j][i], left, left_down,left_up)

  return max(max(d))


ans = []
#t만큼 테스트케이스 반복실행
for _ in range(t):
  ans.append(test_case())
for _ in range(t):
  print(ans[_])

