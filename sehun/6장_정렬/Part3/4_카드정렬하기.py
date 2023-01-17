#풀었는데 정답잘나오나 백준에서는 fail뜸 
#heapq모듈 자체를 몰라서 안썼음..

n = int(input())
card = [int(input()) for _ in range(n)]
card.sort()
count = 0

def make(n, count, card):
  new_card = []
  for i in range(1, n):
    if n%2 == 1 and i == n-1:
      a = new_card[0] + card[i]
      count += a
      new_card[0] = a
      break
    if i%2 == 1:
      a = card[i-1] + card[i]
      count += a
      new_card.append(a)
  return new_card, count, len(new_card)

while n>1:
  card, count, n  = make(n, count, card)

print(count)