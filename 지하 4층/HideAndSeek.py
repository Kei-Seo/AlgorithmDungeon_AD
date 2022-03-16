import sys
from collections import deque, defaultdict
counted = defaultdict(int)

q = deque()
n, k = map(int, sys.stdin.readline().split())
q.append((n, 0))
visit = [False for _ in range(100001)]
cnt = 0

while q:
  p, c = q.popleft()
  visit[p] = True
  
  if p == k:
    counted[c] += 1   
  else:
    if 0 <= p + 1 <= 100000 and not visit[p+1]:
      q.append((p+1, c+1))
    if 0 <= p - 1 <= 100000 and not visit[p-1]:
      q.append((p-1, c+1))
    if 0 <= p * 2 <= 100000 and not visit[p*2]:
      q.append((p*2, c+1))

for key in counted.keys():
  print(key)
  print(counted[key])
  exit(0)
  
print(visit[k])
print(cnt)
  

  
